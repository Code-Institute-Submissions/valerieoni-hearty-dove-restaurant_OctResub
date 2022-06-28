from datetime import datetime, timedelta

from django.shortcuts import render, reverse
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import ReservationForm, CustomerForm
from .models import Table


def get_available_table(no_of_seats, reserve_date, reserve_time):
    """
    returns the total number of tables that are available for reservation.
    This is the total of all tables exclude those
    that have been reserved for the reserved date and time

    Returns integer
    """
    available_tables = Table.objects.filter(
        seat_capacity__gte=no_of_seats).exclude(
        reservation__reservation_date=reserve_date,
        reservation__reservation_time__gte=reserve_time
    )

    return len(available_tables)


class ReservationRequest(View):
    ''' returns reservation form '''
    template_name = 'reservation/reservation_request.html'
  
    def get(self, request, *args, **kwargs):
        """
        display request form which comprises of 
        the customer form and the reservation form
        """
        reservation_form = ReservationForm()
        customer_form = CustomerForm()

        return render(request, self.template_name, {
            'reservation_form': reservation_form,
            'customer_form': customer_form
        })

    def post(self, request, *args, **kwargs):
        """
        validate customer and reservation form.
        check that table can be reserved.
        If reservation can be made, then:
        - save request
        - send email to restaurant recipeint so they know there's a new request
        - display feedback message to customer
        """
        customer_form = CustomerForm(request.POST)
        reservation_form = ReservationForm(request.POST)

        if customer_form.is_valid() and reservation_form.is_valid():
            party_size = request.POST.get('party_size')
            reservation_date = request.POST.get('reservation_date')
            reservation_time = request.POST.get('reservation_time')

            if get_available_table(
                    party_size, reservation_date, reservation_time) > 0:
                customer = customer_form.save()
                reservation = reservation_form.save(commit=False)
                reservation.customer = customer
                reservation.save()

                message = f"""Thank you. You reservation request for
                a party of {party_size} was successfully submitted"""

                messages.add_message(
                    request, messages.SUCCESS, message)

                return HttpResponseRedirect(reverse(
                    'reservation_request'))
            else:
                messages.add_message(
                    request, messages.ERROR,
                    "Thank you for interest. Unfortunately we are fully booked"
                )

        else:
            message = """Request submission failed. Please ensure
            all required fields are filled in"""

            messages.add_message(
                request, messages.SUCCESS, message)

        return render(request, self.template_name, {
            'reservation_form': reservation_form,
            'customer_form': customer_form
        })
