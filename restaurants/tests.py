from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Restaurant, Booking
from datetime import datetime, timedelta
from django.utils import timezone


class RestaurantListTest(TestCase):

    def setUp(self):
        # Create a restaurant to display
        self.restaurant = Restaurant.objects.create(
            name='Test Restaurant',
            address='123 Test Street',
            max_tables=10
        )
        # Create a user and log them in
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_restaurant_list_access(self):
        # Log in the user before accessing the view
        self.client.login(username='testuser', password='password')
        
        response = self.client.get(reverse('restaurant_list'))
        
        # Check the response status and ensure the restaurant name is in the response
        self.assertEqual(response.status_code, 200)
        # Check that restaurant name is displayed
        self.assertContains(response, 'Test Restaurant')

class RestaurantDetailTest(TestCase):

    def setUp(self):
        self.restaurant = Restaurant.objects.create(
            name='Test Restaurant',
            address='123 Test Street',
            max_tables=10
        )

    def test_restaurant_detail_access(self):
        response = self.client.get(reverse('restaurant_detail', args=[self.restaurant.id]))
        self.assertEqual(response.status_code, 200)
        # Does restaurant name appears
        self.assertContains(response, 'Test Restaurant')


class CreateBookingTest(TestCase):

    def setUp(self):
        # Create a user for the test
        self.user = User.objects.create_user(username='testuser', password='password')

        # Create a restaurant for the test
        self.restaurant = Restaurant.objects.create(
            name="Test Restaurant",
            address="123 Test St, Test City",
            description="A test restaurant for bookings.",
            max_tables=10,
            cuisine_type="Italian"
        )

    def test_create_booking_post(self):
        # Create a booking for tomorrow
        response = self.client.post('/create_booking/', {
            'user': self.user.id,
            'restaurant': self.restaurant.id,
            'name': "John Doe",
            'email': "johndoe@example.com",
            'phone_number': "1234567890",
            'date': (datetime.now() + timedelta(days=1)).date(),
            'time': '18:00',
            'party_size': 4, 
        })

    def test_create_booking_invalid_data(self):
        # Try to create a booking with invalid data (e.g., a past date)
        response = self.client.post('/create-booking/', {
            'user': self.user.id,
            'restaurant': self.restaurant.id,
            'name': "John Doe",
            'email': "johndoe@example.com",
            'phone_number': "1234567890",
            'date': (datetime.now() - timedelta(days=1)).date(), 
            'time': '18:00',
            'party_size': 4,
        })

class MyBookingsTest(TestCase):

    def setUp(self):
        # Create a user for the test
        self.user = User.objects.create_user(username='testuser', password='password')

        # Create a restaurant for the test
        self.restaurant = Restaurant.objects.create(
            name="Test Restaurant",
            address="123 Test St, Test City",
            description="A test restaurant for bookings.",
            max_tables=10,
            cuisine_type="Italian"
        )

        # Create a booking for tomorrow
        self.booking = Booking.objects.create(
            user=self.user,
            restaurant=self.restaurant,
            name="John Doe",
            email="johndoe@example.com",
            phone_number="1234567890",
            date=datetime.today().date() + timedelta(days=1),  # Tomorrow's date
            time="18:00",
            party_size=4  # Make sure party_size is included
        )

    def test_my_bookings_access(self):
        # Test that a logged-in user can access their bookings
        self.client.login(username='testuser', password='password')
        response = self.client.get('/my_bookings/')

    def test_cancel_booking(self):
        # Make a POST request to cancel the booking
        response = self.client.post(reverse('cancel_booking', args=[self.booking.id]))
        

    def test_edit_booking_valid_data(self):
    # Post valid data to edit the booking
        new_time = (timezone.now() + timedelta(hours=2)).time()
        response = self.client.post(reverse('edit_booking', args=[self.booking.id]), {
            'name': "Updated Name",
            'email': "updatedemail@example.com",
            'phone_number': "9876543210",
            'time': new_time,
            'date': self.booking.date,
            'party_size': 2
        })

         # Check if the form was valid and processed
        self.assertEqual(response.status_code, 302)  # Expecting a redirect (successful form submission)
    
        # If the form was not valid, print the response content for debugging
        if response.status_code != 302:
            print(response.content)
            form = response.context['form']
            print(form.errors)  # Print form errors to debug why it might not be saving

        # Check that the booking was updated
        self.booking.refresh_from_db()  # Make sure to refresh from DB to get the latest data
        self.assertEqual(self.booking.name, "Updated Booking")
        self.assertEqual(self.booking.email, "updatedemail@example.com")
        self.assertEqual(self.booking.time, new_time)

        # Check that the user is redirected to the 'my_bookings' page
        self.assertRedirects(response, reverse('my_bookings'))


    def test_edit_booking_invalid_data_past_date(self):
        # Try to edit the booking with a time in the past (invalid)
        past_time = (timezone.now() - timedelta(hours=2)).time()  # A time in the past
        response = self.client.post(reverse('edit_booking', args=[self.booking.id]), {
            'name': "Updated Name",
            'email': "updatedemail@example.com",
            'phone_number': "9876543210",
            'date': self.booking.date,
            'time': past_time,
            'party_size': 2
        })

        # Check that the booking is not updated
        self.booking.refresh_from_db()
        self.assertNotEqual(self.booking.time, past_time)
           