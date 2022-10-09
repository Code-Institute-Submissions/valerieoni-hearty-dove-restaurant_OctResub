from reservation import views
from django.urls import path


urlpatterns = [
    path('', views.ReservationRequest.as_view(), name='reservation_request'),
    path('reservation', views.ReservationList.as_view(),
         name='user_reservation'),
    path('delete_reservation/<reservation_id>',
         views.delete_reservation,
         name='delete_reservation'),
    path('update_reservation/<reservation_id>',
         views.ReservationUpdate.as_view(),
         name='update_reservation'),
]
