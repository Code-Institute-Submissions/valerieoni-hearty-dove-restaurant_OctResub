from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


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
        return self.last_name + self.first_name


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
