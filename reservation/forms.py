from .models import Reservation, Customer
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Div


class ReservationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()

    class Meta:
        model = Reservation
        fields = (
            'first_name', 'last_name', 'email', 'party_size',
            'reservation_date', 'reservation_time', 'special_requirement')

    @property
    def helper(self):
        ''' Set form layout using cripy form'''
        helper = FormHelper()
        helper.layout = Layout(
            Div('first_name', 'last_name'),
            Field('email'),
            Field('party_size'),
            Div('reservation_date', 'reservation_time'),
            Field('special_requirement'),
            Submit('submit', 'Request Reservation')
        )
        return helper


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
            'first_name', 'last_name', 'email', 'phone'
        )
