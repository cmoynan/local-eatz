from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Restaurant(models.Model):
    """
    Model for storing information about restaurants.
    """
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    max_tables = models.PositiveIntegerField(default=3)
    cuisine_type = models.CharField(max_length=100, blank=True)

    def __str__(self):
        """
        Return the name of the restaurant as the string representation.
        """
        return self.name


class Booking(models.Model):
    """
    Model for storing booking details.
    """
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True)
    date = models.DateField()
    time = models.TimeField()
    party_size = models.PositiveIntegerField()
    special_requests = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        String representation of the booking.
        """
        return (
            f"Booking for {self.name} at {self.restaurant.name} "
            f"on {self.date} at {self.time}, Party Size: {self.party_size}"
        )
