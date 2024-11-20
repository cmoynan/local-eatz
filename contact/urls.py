from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.contact, name='contact'),
    path('customer/', views.customer_inquiry_view, name='customer_inquiry'),
    path('business/', views.business_inquiry_view, name='business_inquiry'),
    path('thank-you/', views.thank_you_view, name='thank_you'),
]
