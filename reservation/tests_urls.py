from django.test import TestCase
from django.urls import reverse


class TestUrls(TestCase):
    def test_reservation_url_is_resolved(self):
        """Test reservation request is resolved"""
        response = self.client.get(reverse('reservation_request'))
        self.assertEqual(response.status_code, 200)
