from django import forms
from .models import BusinessInquiry, CustomerInquiry


class CustomerContactForm(forms.ModelForm):
    class Meta:
        model = CustomerInquiry
        fields = ['name', 'email', 'message']


class BusinessInquiryForm(forms.ModelForm):
    class Meta:
        model = BusinessInquiry
        fields = ['name', 'email', 'phone_number', 'restaurant_name', 'address',
                  'description', 'cuisine_type', 'max_tables']
