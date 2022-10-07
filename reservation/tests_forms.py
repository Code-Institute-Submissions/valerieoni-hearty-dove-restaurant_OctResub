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

    def test_phone_is_not_required(self):
        """
        Test the phone field is not required
        """
        form = CustomerForm({'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertNotIn('phone', form.errors.keys())

    def test_customer_form_is_valid(self):
        """Test that form is valid when all required fields
        ('first_name', 'last_name', 'email') are filled in correctly"""
        form = CustomerForm({
            'first_name': 'afoke',
            'last_name': 'osa',
            'email': 'afoke.osa@yahoo.com'
        })
        self.assertTrue(form.is_valid())
  
    def test_firstname_is_required(self):
        """
        Test the first_name field is not empty
        """
        form = CustomerForm({
            'first_name': '',
            'last_name': 'osa',
            'email': 'afoke.osa@yahoo.com'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())

    def test_email_is_required(self):
        """
        Test the first_name field is not empty
        """
        form = CustomerForm({
            'first_name': 'afoke',
            'last_name': 'osa',
            'email': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())

    def test_lastname_is_required(self):
        """
        Test the first_name field is not empty
        """
        form = CustomerForm({
            'first_name': 'afoke',
            'last_name': '',
            'email': 'afoke.osa@yahoo.com'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors.keys())


class TestReservationForm(TestCase):
    '''Test reservation form'''
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
