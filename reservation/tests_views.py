from django_webtest import WebTest
from django.urls import reverse
import datetime


class ReservationRequestTest(WebTest):
    '''Test make reservation web page'''   
    def test_page_contains_form(self):
        '''Test page contains reservation form'''
        page = self.app.get(reverse('reservation_request'))
        self.assertEqual(len(page.forms), 1)

    def test_reservation_form_error(self):
        '''
        test empty form submission returns field required error
        '''
        page = self.app.get(reverse('reservation_request'))
        page = page.form.submit()
        self.assertContains(page, "field is required")

    def test_reservation_form_success(self):
        '''test form submits successfully'''
        page = self.app.get(reverse('reservation_request'))
        page = page.form.submit()
        page.form['last_name'] = 'Test'
        page.form['first_name'] = 'User'
        page.form['email'] = 'test.user@test.com'
        page.form['reservation_date'] = datetime.date.today()
        page.form['reservation_time'] = '11:00'
        page.form['party_size'] = 4
        page = page.form.submit()
        self.assertEqual(page.status_code, 200)
