from django.contrib import admin
from .models import MealCategory, Meal

@admin.register(MealCategory)
class MealCategoryAdmin(admin.ModelAdmin):
    list_filter = ('updated_on', 'title')
    list_display = ('title', 'available_from', 'available_until', 'updated_on')


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_filter = ('is_available', 'meal_category')
    search_fields = ['meal_name', 'meal_category']
    list_display = ('meal_name', 'meal_category', 'price', 'is_available', 'updated_on')
