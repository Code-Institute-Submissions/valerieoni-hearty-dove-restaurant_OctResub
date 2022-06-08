from django.db import models


class MealCategory(models.Model):
    """
    Meal category model
    """
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    available_from = models.TimeField()
    available_until = models.TimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Meal(models.Model):
    """
    Meal model
    """
    meal_name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    meal_category = models.ForeignKey(MealCategory, on_delete=models.CASCADE, related_name='meal_category')
    dietary_info = models.TextField(blank=True)
    allergy_info = models.TextField(blank=True)
    price = models.FloatField()
    is_available = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_available', '-meal_category']

    def __str__(self):
        return self.meal_name


class DrinkCategory(models.Model):
    """
    Drink category model
    """
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Drink(models.Model):
    """
    Drink model
    """
    drink_name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    drink_category = models.ForeignKey(DrinkCategory, on_delete=models.CASCADE)
    dietary_info = models.TextField(blank=True)
    allergy_info = models.TextField(blank=True)
    price = models.FloatField()
    is_available = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_available', '-drink_category']

    def __str__(self):
        return self.drink_name
