from django.urls import path
from menu import views

app_name = 'menu'
urlpatterns = [
    path('', views.MealList.as_view(), name='meal_list'),
    path('drinks', views.DrinksList.as_view(), name='drinks')
]
