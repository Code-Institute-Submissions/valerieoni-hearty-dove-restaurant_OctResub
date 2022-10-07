from django import forms
from .models import Reservation, Customer
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Field


class ReservationForm(forms.ModelForm):
    """Reservation form"""
    
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
                Column('party_size'),
                Column(Field('reservation_date', placeholder="Enter date",
                             css_class='datepicker')),
                Column(Field('reservation_time', placeholder="Example: 16:00"))
            ),
            Row(
                Column('special_requirement')
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
                Column('phone')
            )
        )
