import datetime

from django.test import TestCase, Client

from .models import Reservation, Customer


class ReservationRequestTest(TestCase):
    def setup(self):
        self.client = Client()
        self.customer = Customer.objects.create(
            last_name='Test',
            first_name='User',
            email='test.user@test.com'
        )
        self.reservation_date = datetime.date.today()
        self.reserve_time = "11:00"
        self.reservation = Reservation.objects.create(
            customer=self.customer,
            reservation_date=self.reservation_date,
            reservation_time=self.reserve_time,
            party_size=4
        )

    def test_request_made_is_not_in_the_past(self):
        """
        check that a reservation date
        is not in the past
        """

    def test_cannot_book_when_no_table_available(self):
        """
        test that a reservation cannot be made
        when there is not enough tables 
        """