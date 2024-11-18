from django.db import models

# Create your models here.


class BusinessInquiry(models.Model):
    """
    Model to store business inquiries from businesses wishing to list on the platform.
    """
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True)
    restaurant_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    cuisine_type = models.CharField(max_length=100, blank=True)
    max_tables = models.PositiveIntegerField(default=3)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.restaurant_name} - {self.name}"