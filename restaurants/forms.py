from django import forms
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Booking
from crispy_forms.helper import FormHelper
import datetime


class BookingForm(forms.ModelForm):
    def __init__(self, *args, available_time_slots=None, **kwargs):
        super().__init__(*args, **kwargs)

        if available_time_slots is not None:
            self.fields['time'].widget = forms.Select(
             choices=[(slot, slot) for slot in available_time_slots]
            )

        self.fields['party_size'].validators.extend([
            MinValueValidator(
             1, message="The party size must be at least 1 person."
            ),
            MaxValueValidator(
             10, message="The party size cannot exceed 10 people."
            )

        ])

    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone_number', 'date', 'time',
                  'party_size', 'special_requests']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'special_requests': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_party_size(self):
        party_size = self.cleaned_data.get('party_size')

        if party_size < 1:
            raise ValidationError("The party size must be at least 1 person.")
        elif party_size > 10:
            raise ValidationError("The party size cannot exceed 10 people.")

        return party_size

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        if date and time:
            current_datetime = timezone.now()

            booking_datetime = timezone.make_aware(
              datetime.datetime.combine(date, time)
             )

            if booking_datetime < current_datetime:
                self.add_error('date', 'You cannot book a table in the past.')
                self.add_error('time', 'You cannot book a table in the past.')

        return cleaned_data
