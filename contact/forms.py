from django import forms
from .models import BusinessInquiry

class CustomerContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class BusinessInquiryForm(forms.ModelForm):
    class Meta:
        model = BusinessInquiry
        fields = ['name', 'email', 'phone_number', 'restaurant_name', 'description', 'cuisine_type', 'max_tables']
