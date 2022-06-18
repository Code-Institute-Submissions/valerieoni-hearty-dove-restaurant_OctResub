from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import BadHeaderError, send_mail
from .forms import ContactForm


def email_enquiry(form):
    """
    takes an instance of ContactForm as input parameter
    sets subject and other email parameters and sends email
    returns True if email was succesfully sent
    """
    form_data = form.cleaned_data
    customer_name = form_data['customer_name']
    customer_email = form_data['customer_email']
    message = form_data['message']
    subject = (f'Customer Enquiry from {customer_name}')
    recipients = ['valeriewil@yahoo.com']

    try:
        send_mail(subject, message, customer_email, recipients)
    except BadHeaderError:
        return False
    return True


def index(request):
    """displays home page of the restaurant's website"""
    return render(request, 'restaurant/index.html')


def contact(request):
    """
    Renders contact us page.
    if POST request, validates form,
    sends an enquiry email and return feedback to user.
    Otherwise, if GET request create a blank ContactForm. 
    """
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            submitted = email_enquiry(form)
            return HttpResponseRedirect(f'/contact?submitted={submitted}')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'restaurant/contact.html', {'form': form, 'submitted': submitted})
