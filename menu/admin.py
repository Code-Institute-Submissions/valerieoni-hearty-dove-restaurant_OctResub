from django.contrib import admin
from .models import MealCategory, Meal, DrinkCategory, Drink


@admin.register(MealCategory)
class MealCategoryAdmin(admin.ModelAdmin):
    list_filter = ('updated_on', 'title')
    list_display = ('title', 'available_from', 'available_until', 'updated_on')


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_filter = ('is_available', 'meal_category')
    search_fields = ['meal_name', 'meal_category']
    list_display = ('meal_name', 'meal_category', 'price', 'is_available', 'updated_on')


@admin.register(DrinkCategory)
class DrinkCategoryAdmin(admin.ModelAdmin):
    list_filter = ('drink_type', 'title')
    list_display = ('drink_type', 'title')


@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_filter = ('is_available', 'drink_category')
    search_fields = ['drink_name', 'drink_category']
    list_display = ('drink_name', 'drink_category', 'price', 'is_available')
