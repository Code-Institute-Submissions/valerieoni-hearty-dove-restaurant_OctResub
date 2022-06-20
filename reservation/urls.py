from reservation import views
from django.urls import path


urlpatterns = [
    path('', views.ReservationRequest.as_view(), name='reservation_request'),
    ]
