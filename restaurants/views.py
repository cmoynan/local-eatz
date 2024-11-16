from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Restaurant, Booking
from datetime import date

# Create your views here.

@login_required
def restaurant_list(request):
    """
    View to list all restaurants.
    """
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/restaurant_list.html', {'restaurants': restaurants})


def restaurant_detail(request, id):
    """
    View to display details of a single restaurant.
    """
    restaurant = get_object_or_404(Restaurant, pk=id)
    return render(request, 'restaurants/restaurant_detail.html', {'restaurant': restaurant})


@login_required
def create_booking(request, restaurant_id):
    """
    View to create a new booking.
    Requires the user to be logged in.
    """
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            # Save the booking instance
            booking = form.save(commit=False)
            booking.user = request.user
            booking.restaurant = restaurant

            # Check availability logic
            existing_bookings = Booking.objects.filter(
                restaurant=restaurant, date=booking.date, time=booking.time
            ).count()

            if existing_bookings < restaurant.max_tables:
                booking.save()
                messages.success(request, "Your booking was successfully created!")
                return redirect('my_bookings')
            else:
                messages.error(
                    request,
                    "Unfortunately, the restaurant is fully booked at this time. Please try another slot."
                )
    else:
        form = BookingForm()

    return render(request, 'create_booking.html', {'form': form, 'restaurant': restaurant})


@login_required
def my_bookings(request):
    """
    View to list all bookings made by the logged-in user.
    """
    bookings = Booking.objects.filter(user=request.user).order_by('-date', '-time')
    return render(request, 'my_bookings.html', {'bookings': bookings})


@login_required
def cancel_booking(request, booking_id):
    """
    View to cancel a booking.
    """
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)

    if request.method == "POST":
        booking.delete()
        messages.success(request, "Your booking was successfully canceled.")
        return redirect('my_bookings')

    return render(request, 'cancel_booking.html', {'booking': booking})

