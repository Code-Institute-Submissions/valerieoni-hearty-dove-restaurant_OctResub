from django.shortcuts import render


def index(request):
    """displays home page of the restaurant's website"""
    return render(request, 'restaurant/index.html')
