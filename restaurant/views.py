from django.shortcuts import render


def index(request):
    """displays home page of the restaurant's website"""
    return render(request, 'restaurant/index.html')

def contact(request):
    """ displays contact us page"""
    return render(request, 'restaurant/contact.html')
