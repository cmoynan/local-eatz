from django.urls import path
from . import views

urlpatterns = [
    # URL for viewing the list of restaurants
    path('', views.restaurant_list, name='restaurant_list'),
    
    # URL for viewing the booking page for a specific restaurant
    path('restaurant/<int:restaurant_id>/book/', views.create_booking, name='create_booking'),

    path('restaurant/<int:id>/', views.restaurant_detail, name='restaurant_detail'),
]