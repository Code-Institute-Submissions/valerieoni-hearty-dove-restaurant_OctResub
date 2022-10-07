from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

times_available = (
    ("10:00", "10:00"),
    ("10:30", "10:30"),
    ("11:00", "11:00"),
    ("11:30", "11:30"),
    ("12:00", "12:00"),
    ("12:30", "12:30"),
    ("13:00", "13:00"),
    ("13:30", "13:30"),
    ("14:00", "14:00"),
    ("14:30", "14:30"),
    ("15:00", "15:00"),
    ("15:30", "15:30"),
    ("16:00", "16:00"),
    ("16:30", "16:30"),
    ("17:00", "17:00"),
    ("17:30", "17:30"),
    ("18:00", "18:00"),
    ("18:30", "18:30"),
    ("19:00", "19:00"),
    ("19:30", "19:30"),
    ("20:00", "20:00"),
    ("20:30", "20:30"),
    ("21:00", "21:00"),
    )

class Customer(models.Model):
    '''Customer object'''
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    phone = PhoneNumberField(blank=True)
    create_date = models.DateField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return f'{self.last_name}  {self.first_name}'


class Table(models.Model):
    ''' Table object '''
    table_name = models.CharField(max_length=50, unique=True)
    seat_capacity = models.IntegerField(default=2)
    position = models.CharField(max_length=200, blank=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ['-available']

    def __str__(self):
        ''' returns table name'''
        return self.table_name


class Reservation(models.Model):
    ''' Reservation object '''
    STATUS = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    party_size = models.IntegerField(default=1)
    special_requirement = models.TextField(max_length=200, blank=True)
    status = models.CharField(
        max_length=10, choices=STATUS, default='pending')
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
