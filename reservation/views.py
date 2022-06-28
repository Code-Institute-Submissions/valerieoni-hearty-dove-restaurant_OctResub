from django.shortcuts import render, reverse
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ReservationForm, CustomerForm


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
            customer = customer_form.save()
            reservation = reservation_form.save(commit=False)
            reservation.customer = customer
            reservation.save()

            return HttpResponseRedirect(reverse(
                'reservation_request'))
        else:
            return render(request, self.template_name, {
                'reservation_form': reservation_form,
                'customer_form': customer_form
            })
