from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Field
from .models import Reservation, Customer, times_available


class ReservationForm(forms.ModelForm):
    """Reservation form"""
    reservation_time = forms.ChoiceField(choices=times_available)   

    class Meta:
        model = Reservation
        fields = [
            'party_size', 'reservation_date',
            'reservation_time', 'special_requirement'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

        self.helper.layout = Layout(
            Row(
                Column(Field('party_size', max=6)),
                Column(Field('reservation_date', placeholder="Enter date",
                             css_class='datepicker')),
                Column(Field('reservation_time'))
            ),
            Row(
                Column(Field('special_requirement', rows=3))
            )
        )


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = [
            'first_name', 'last_name', 'email', 'phone'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('first_name'),
                Column('last_name')
            ),
            Row(
                Column('email'),
                Column(Field('phone', placeholder="Format: +44"))
            )
        )


class ManageReservationForm(forms.Form):
    """Manage reservation form"""
    customer_name = forms.CharField(max_length=50, label='Last Name')
    customer_email = forms.EmailField(max_length=100, label='Email Address')
