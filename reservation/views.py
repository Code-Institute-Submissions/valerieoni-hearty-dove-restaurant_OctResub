from django.shortcuts import render
from django.views import generic, View
from .models import Reservation
from .forms import ReservationForm, CustomerForm


class ReservationRequest(View):
    ''' returns reservation form '''

    def get(self, request, *args, **kwargs):
        form_class = ReservationForm()
        template_name = 'reservation/reservation_request.html'

        return render(request, template_name, {
            'form_class': form_class})
