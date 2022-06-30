from reservation import views
from django.urls import path


urlpatterns = [
    path('', views.ReservationRequest.as_view(), name='reservation_request'),
    path('reservation', views.ReservationList.as_view(),
         name='user_reservation'),
    path('<id>/delete_reservation', views.ReservationDelete.as_view(),
         name='delete_reservation'),
]
