from django.contrib import admin
from .models.meals import Meal, Category as MealCategory
from .models.drinks import Drink, DrinkCategory


@admin.register(MealCategory)
class MealCategoryAdmin(admin.ModelAdmin):
    list_filter = ('updated_on', 'title')
    list_display = ('title', 'available_from', 'available_until', 'updated_on')


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_filter = ('is_available', 'category')
    search_fields = ['meal_name', 'category__title']
    list_display = ('meal_name', 'category', 'price',
                    'is_available', 'updated_on')


@admin.register(DrinkCategory)
class DrinkCategoryAdmin(admin.ModelAdmin):
    list_filter = ('drink_type', 'title')
    list_display = ('drink_type', 'title')


@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_filter = ('is_available', 'drink_category')
    search_fields = ['drink_name', 'drink_category__title']
    list_display = ('drink_name', 'drink_category', 'price', 'is_available')
