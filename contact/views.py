from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomerContactForm, BusinessInquiryForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def contact(request):
    """
    This view renders a page asking whether the user is a customer or a business
    and then displays the appropriate form based on the selection.
    """
    if request.method == 'POST':
        contact_type = request.POST.get('contact_type')
        if contact_type == 'business':
            return redirect('contact:business_inquiry')
        else:
            return redirect('contact:customer_inquiry')

    return render(request, 'contact/contact.html')

def customer_inquiry_view(request):
    """
    This view handles the customer contact form submission.
    """
    if request.method == 'POST':
        form = CustomerContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact:thank_you')
        else:
            messages.error(request, 'There was an error with your form.')

    else:
        form = CustomerContactForm()

    return render(request, 'contact/customer_inquiry.html', {'form': form})

def business_inquiry_view(request):
    """
    This view handles the business inquiry form submission.
    """
    if request.method == 'POST':
        form = BusinessInquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your business inquiry has been submitted.')
            return redirect('contact:thank_you')
        else:
            messages.error(request, 'There was an error with your form.')

    else:
        form = BusinessInquiryForm()

    return render(request, 'contact/business_inquiry.html', {'form': form})

def thank_you_view(request):
    """
    Thank you page after form submission.
    """
    return render(request, 'contact/thank_you.html')
