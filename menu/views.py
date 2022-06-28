from django.views import generic
from .models.meals import Category, Meal
from .models.drinks import DrinkCategory, Drink


class MealList(generic.ListView):
    template_name = 'menu/meal_list.html'
    context_object_name = 'meal_list'

    def get_queryset(self):
        categories = Category.objects.select_related().filter(
            meals__is_available=True)
        queryset = {'categories': categories}
        return queryset


class DrinksList(generic.ListView):
    template_name = 'menu/drinks.html'
    context_object_name = 'drinks_list'

    def get_queryset(self):
        categories = DrinkCategory.objects.select_related().filter(
            drinks__is_available=True
        )
        return {'categories': categories}
