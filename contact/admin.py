from django.contrib import admin
from .models import BusinessInquiry


# Register your models here.
class BusinessInquiryAdmin(admin.ModelAdmin):
    list_display = ('restaurant_name', 'name', 'email', 'created_at')
    search_fields = ('restaurant_name', 'name', 'email')

admin.site.register(BusinessInquiry, BusinessInquiryAdmin)