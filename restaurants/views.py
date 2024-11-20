from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Restaurant, Booking
from datetime import date
from .forms import BookingForm
from django.db.models import Count
from django.utils import timezone
from django.utils.timezone import now
import datetime
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


# Create your views here.


@login_required
def restaurant_list(request):
    """
    View to list all restaurants.
    """
    restaurants = Restaurant.objects.all()
    return render(request,
                  'restaurants/restaurant_list.html',
                  {'restaurants': restaurants})


def restaurant_detail(request, id):
    """
    View to display details of a single restaurant.
    """
    restaurant = get_object_or_404(Restaurant, pk=id)
    return render(request, 'restaurants/restaurant_detail.html',
                  {'restaurant': restaurant})


@login_required
def create_booking(request, restaurant_id):
    """
    View to create a new booking.
    Requires the user to be logged in.
    """
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

    current_datetime = datetime.datetime.now()

    available_time_slots = [
        slot for slot in [datetime.time(hour) for hour in range(12, 22)]
        if Booking.objects.filter(restaurant=restaurant,
                                  date=request.POST.get('date'),
                                  time=slot).count() < restaurant.max_tables
    ]

    if request.method == "POST":
        form = BookingForm(request.POST,
                           available_time_slots=available_time_slots)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.restaurant = restaurant

            booking_datetime = datetime.datetime.combine(booking.date,
                                                         booking.time)
            if booking_datetime < current_datetime:
                messages.error(request,
                               "You cannot book a table in the past.")
            else:

                existing_bookings = Booking.objects.filter(
                    restaurant=restaurant, date=booking.date, time=booking.time
                ).count()

                if existing_bookings < restaurant.max_tables:
                    booking.save()
                    messages.success(request,
                                     "Your booking was successfully created!")

                    booking_details = {
                      'user': request.user,
                      'booking': booking
                    }

                    # Send booking Confirmation email
                    subject = 'Booking Confirmation'
                    html_message = render_to_string(
                     'emails/booking_confirmation.html', booking_details,
                    )

                    plain_message = strip_tags(html_message)
                    send_mail(subject, plain_message,
                              settings.DEFAULT_FROM_EMAIL,
                              [request.user.email], html_message=html_message)

                    return redirect('booking_success', booking_id=booking.id)
                else:
                    messages.error(
                        request,
                        "Unfortunately, the restaurant is fully \
                          booked at this time.Please try another slot."

                    )
        else:
            messages.error(request,
                           "There was an issue with your form. \
                           Please check the details and try again.")
    else:
        form = BookingForm(available_time_slots=available_time_slots)

    return render(request, 'restaurants/create_booking.html',
                  {'form': form, 'restaurant': restaurant})


def booking_success(request, booking_id):
    """
    View to display booking success details.
    """
    booking = get_object_or_404(Booking, pk=booking_id)
    return render(request,
                  'restaurants/booking_success.html', {'booking': booking})


@login_required
def my_bookings(request):
    """
    View to list all bookings made by the logged-in user.
    """
    bookings = Booking.objects.filter(user=request.user) \
        .order_by('-date', '-time')

    return render(request, 'restaurants/my_bookings.html',
                  {'bookings': bookings})


@login_required
def cancel_booking(request, booking_id):
    """
    View to cancel a booking.
    """
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)

    if request.method == "POST":
        booking.delete()
        messages.success(request, "Your booking was successfully canceled.")

        booking_details = {
         'user': request.user,
         'booking': booking
        }

        # Send booking cancellation email
        subject = 'Booking Cancellation'
        html_message = render_to_string(
         'emails/booking_cancellation.html', booking_details,
        )

        plain_message = strip_tags(html_message)
        send_mail(subject, plain_message, settings.DEFAULT_FROM_EMAIL,
                  [request.user.email], html_message=html_message)

        return redirect('my_bookings')

    return render(request, 'restaurants/cancel_booking.html',
                  {'booking': booking})


@login_required
def edit_booking(request, booking_id):
    """
    View to edit an existing booking.
    Requires the user to be logged in and the booking to belong to the user.
    """
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    restaurant = booking.restaurant

    current_datetime = datetime.datetime.now()

    available_time_slots = [
        slot for slot in [datetime.time(hour) for hour in range(12, 22)]
        if (Booking.objects.filter(
         restaurant=restaurant,
         date=request.POST.get('date'),
         time=slot
        ).count() < restaurant.max_tables)

    ]

    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking,
                           available_time_slots=available_time_slots)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.restaurant = restaurant
            booking.user = request.user

            booking_datetime = datetime.datetime.combine(booking.date,
                                                         booking.time)
            if booking_datetime < current_datetime:
                messages.error(request,
                               "You cannot book a table in the past.")
            else:

                existing_bookings = Booking.objects.filter(
                    restaurant=restaurant, date=booking.date, time=booking.time
                ).count()

                if existing_bookings < restaurant.max_tables:
                    booking.save()
                    messages.success(request,
                                     "Your booking was successfully updated!")

                    booking_details = {
                     'user': request.user,
                     'booking': booking
                    }

                    # Send booking update email
                    subject = 'Booking Update'
                    html_message = render_to_string(
                     'emails/booking_update.html', booking_details,
                    )

                    plain_message = strip_tags(html_message)
                    send_mail(subject, plain_message,
                              settings.DEFAULT_FROM_EMAIL,
                              [request.user.email], html_message=html_message)

                    return redirect('my_bookings')
                else:
                    messages.error(
                        request,
                        "The restaurant is fully booked at this time."
                    )
        else:
            messages.error(request,
                           "There was an issue with your form. \
                            Please check the details and try again.")
    else:
        form = BookingForm(instance=booking,
                           available_time_slots=available_time_slots)

    return render(request, 'restaurants/edit_booking.html',
                  {'form': form, 'restaurant': restaurant, 'booking': booking})
