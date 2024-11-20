from django.contrib import admin
from .models import BusinessInquiry, CustomerInquiry


# Register your models here.


@admin.register(CustomerInquiry)
class CustomerInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    search_fields = ('name', 'email')
    readonly_fields = ('name', 'email', 'message', 'submitted_at')


class BusinessInquiryAdmin(admin.ModelAdmin):
    list_display = ('restaurant_name', 'name', 'email', 'created_at')
    search_fields = ('restaurant_name', 'name', 'email')


admin.site.register(BusinessInquiry, BusinessInquiryAdmin)
