from django.contrib import admin
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
    actions = ['inform_user']
    