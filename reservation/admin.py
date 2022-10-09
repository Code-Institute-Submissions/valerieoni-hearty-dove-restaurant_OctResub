from django.contrib import admin
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
        for reservation in queryset:
            if reservation.customer.email:
                message = "Thank you for your interest in our restaurant"
                from_email = settings.EMAIL_HOST_USER
                if reservation.status == 'pending':
                    status_msg = "We are working on your request and will get back to you soon."
                elif reservation.status == 'confirm':
                    status_msg = f"""Your reservatio for the {reservation.reservation_date}
                                  is confirmed. We look forward to welcoming you."""
                else:
                    status_msg = f"""We are sorry, but we are unable to reserve 
                                a table for the {reservation.reservation_date} because
                                we are fully booked at this time."""
                try:
                     send_mail("Reservation Request", f'{message} {status_msg}',
                          from_email, [reservation.customer.email])
                except BadHeaderError:
                    return False
                return True
