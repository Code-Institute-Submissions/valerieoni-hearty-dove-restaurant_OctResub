from django.shortcuts import render, reverse, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import messages
import datetime
from .forms import ReservationForm, CustomerForm
from .models import Table, Customer, Reservation


def get_customer(self, request):
    """
    returns customer object if the user is authenticated
    otherwise redirect to reservation page
    """
    if self.request.user.is_authenticated:
        customer_email = self.request.user.email
        customer = get_object_or_404(
            Customer.objects.filter(email=customer_email))
        return customer
    else:
        return HttpResponseRedirect(reverse('reservation_request'))


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
        creats a new request.
        validate customer and reservation form.
        check that table can be reserved.
        If reservation can be made, then:
        - save customer record if it doesn't already exist
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
            customer_email = request.POST.get('email')

            if get_available_table(
                    party_size, reservation_date, reservation_time) > 0:

                customer_count = Customer.objects.filter(
                    email=customer_email).count()

                if customer_count == 0:
                    customer = customer_form.save()
                else:
                    customer = Customer.objects.get(email=customer_email)

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
                request, messages.ERROR, message)

        return render(request, self.template_name, {
            'reservation_form': reservation_form,
            'customer_form': customer_form
        })


class ReservationList(View):
    current_date = datetime.date.today()
    current_time = datetime.datetime.now().strftime('%H:%M:%S')

    def get(self, request, *args, **kwargs):
        '''
        returns customer's details and reservations
        if user is authenticated otherwise redirect to reservation request page
        '''
        customer_object = get_customer(self, request)

        upcoming_reservations = Reservation.objects.filter(
            customer=customer_object, reservation_date__gte=self.current_date,
            reservation_time__gte=self.current_time)

        past_reservations = Reservation.objects.filter(
            customer=customer_object, reservation_date__lte=self.current_date,
            reservation_time__gte=self.current_time)

        context = {
            'customer': customer_object,
            'upcoming_reservations': upcoming_reservations,
            'past_reservations': past_reservations
        }
        return render(
            request, 'reservation/user_reservation.html', context
        )


class ReservationDelete(View):
    def post(self, request):
        current_date = datetime.date.today()
        customer = get_customer(self, request)
        reservation = get_object_or_404(Reservation.objects.filter(
            pk=request.id, email=customer.email, reservation_date__gt=current_date))
        reservation_date = reservation.reservation_date
        reservation.delete()
        messages.add_message(request, messages.SUCCESS,
                             f"Reservation for { reservation_date} successfully deleted")

        return HttpResponseRedirect(reverse('reservation_request'))
