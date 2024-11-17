from django.urls import path
from . import views

urlpatterns = [
    # URL for viewing the list of restaurants
    path('', views.restaurant_list, name='restaurant_list'),
    
    # URL for viewing the booking page for a specific restaurant
    path('restaurant/<int:restaurant_id>/book/', views.create_booking, name='create_booking'),

    path('restaurant/<int:id>/', views.restaurant_detail, name='restaurant_detail'),
    path('booking-success/<int:booking_id>/', views.booking_success, name='booking_success'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('booking/<int:booking_id>/edit/', views.edit_booking, name='edit_booking'),
]