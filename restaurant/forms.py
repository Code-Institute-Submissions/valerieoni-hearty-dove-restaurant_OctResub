from django import forms


class ContactForm(forms.Form):
    """Contact us form"""
    customer_name = forms.CharField(max_length=100, label='Name',
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    customer_email = forms.EmailField(label='Email address',
                                      widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control'}))
