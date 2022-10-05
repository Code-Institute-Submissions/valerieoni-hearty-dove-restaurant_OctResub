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

    def test_firstname_is_required(self):
        """
        Test the first_name field is not empty
        """
        form = CustomerForm({'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())

    def test_phone_is_not_required(self):
        """
        Test the phone field is not required
        """
        form = CustomerForm({'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertNotIn('phone', form.errors.keys())

    def test_all_fields(self):
        '''
        Test form is valid
        '''
        form = CustomerForm({'first_name': 'Lagbaja',
                            'last_name': 'Wole', 'email': 'info@test.io'})
        self.assertTrue(form.is_valid())


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
