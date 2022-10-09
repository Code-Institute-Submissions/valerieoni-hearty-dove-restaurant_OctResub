from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from .models import Customer, Table, Reservation


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email', 'phone')
    search_fields = ['email', 'last_name', 'first_name']


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_name', 'seat_capacity', 'available')


@admin.register(Reservation)
class Reservation(admin.ModelAdmin):
    list_filter = ('status',)
    list_display = (
        'id', 'customer', 'party_size', 'reservation_date',
        'reservation_time', 'status')
    actions = ['send_user_email']
    
    def send_user_email(self, request, queryset):
        total_sent = 0
        for reservation in queryset:
            if reservation.customer.email:
                message = "Thank you for your interest in our restaurant\n"
                from_email = settings.EMAIL_HOST_USER
                if reservation.status.lower() == 'pending':
                    status_msg = "We are working on your request."
                elif reservation.status.lower() == 'confirmed':
                    status_msg = f"Your reservation for the {reservation.reservation_date}"
                    status_msg = f"{status_msg} is confirmed. We look forward to seeing you."
                else:
                    status_msg = "We are sorry, but we are unable to reserve"
                    status_msg = f" {status_msg} a table for {reservation.reservation_date}"
                    status_msg = f" {status_msg} we are fully booked at this time."
                try:
                    send_mail("Reservation Request", f'{message} {status_msg}',
                              from_email, [reservation.customer.email])
                    total_sent = total_sent + 1
                except BadHeaderError:
                    return False
        self.message_user(request, ngettext(
            '%d message was successfully sent successfully.',
            '%d messages were successfully sent successfully.',
            total_sent,
        ) % total_sent, messages.SUCCESS)

