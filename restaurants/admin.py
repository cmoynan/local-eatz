from django.contrib import admin
from .models import Restaurant, Booking

# Register your models here.


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'cuisine_type',
                    'max_tables', 'description')
    search_fields = ('name', 'address', 'cuisine_type')
    list_filter = ('cuisine_type', 'max_tables')
    list_per_page = 10


class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'date', 'time', 'party_size', 'user')
    search_fields = ('name', 'restaurant__name', 'user__username',
                     'email', 'phone_number')
    list_filter = ('restaurant', 'date', 'time', 'party_size')
    list_per_page = 10


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Booking, BookingAdmin)
