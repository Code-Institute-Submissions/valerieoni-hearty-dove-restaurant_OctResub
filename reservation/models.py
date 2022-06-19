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
