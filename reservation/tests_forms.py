from django.test import TestCase
from .forms import CustomerForm, ReservationForm


class TestCustomerForm(TestCase):

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Test the form only contains the fields 
        first_name, last_name, email, phone
        """
        form = CustomerForm()
        fields = ['first_name', 'last_name', 'email', 'phone']
        self.assertEqual(form.Meta.fields, fields)


class TestReservationForm(TestCase):

    def test_fields_are_explicit_in_metaclass(self):
        """
        Test form only contains the fields
        party size, reservation date, reservation time,
        and special requirement
        """
        form = ReservationForm()
        fields = [
            'party_size', 'reservation_date', 'reservation_time',
            'special_requirement'
        ]
        self.assertEqual(form.Meta.fields, fields)
