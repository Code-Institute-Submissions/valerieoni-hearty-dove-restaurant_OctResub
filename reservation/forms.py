from .models import Reservation, Customer
from django import forms


class ReservationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()

    class Meta:
        model = Reservation
        fields = (
            'first_name', 'last_name', 'email', 'party_size',
            'reservation_date', 'reservation_time', 'special_requirement')


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
            'first_name', 'last_name', 'email', 'phone'
        )
