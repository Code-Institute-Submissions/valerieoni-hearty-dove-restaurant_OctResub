from django.shortcuts import render
from django.views import generic
from .models.meals import Category, Meal


class MealList(generic.ListView):
    template_name = 'meal_list.html'
    context_object_name = 'meal_list'

    def get_queryset(self):
        categories = Category.objects.select_related().filter(
            meals__is_available=True)
        queryset = {category.title: category.meals.all() for category in categories}
        return queryset

