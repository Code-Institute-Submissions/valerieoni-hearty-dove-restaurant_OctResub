from django.urls import path
from menu import views

urlpatterns = [
    path('', views.MealList.as_view(), name='meal_list'),
]
