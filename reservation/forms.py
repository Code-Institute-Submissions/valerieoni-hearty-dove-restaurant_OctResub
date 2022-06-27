from django import forms
from .models import Reservation, Customer


class ReservationForm(forms.ModelForm):
    """Reservation form"""
    class Meta:
        model = Reservation
        fields = [
            'party_size', 'reservation_date', 'reservation_time',
            'special_requirement'
        ]


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'first_name', 'last_name', 'email', 'phone'
        ]
