from django.test import TestCase
from django.urls import reverse, resolve
from restaurant.views import index, contact


class TestUrls(TestCase):
    def test_index_url_is_resolved(self):
        """Test index page is resolved"""
        url = reverse('restaurant:index')
        self.assertEquals(resolve(url).func, index)

    def test_contact_url_is_resolved(self):
        """Test index page is resolved"""
        url = reverse('restaurant:contact')
        self.assertEquals(resolve(url).func, contact)
