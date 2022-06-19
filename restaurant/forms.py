from django import forms


class ContactForm(forms.Form):
    """Contact us form"""
    customer_name = forms.CharField(max_length=100, label='Name')
    customer_email = forms.EmailField(max_length=50, label='Email address')
    message = forms.CharField(widget=forms.Textarea)
