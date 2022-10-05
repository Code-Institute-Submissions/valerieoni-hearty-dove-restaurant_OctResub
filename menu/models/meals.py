from django.db import models


class Category(models.Model):
    """
    schema for meal category model
    """
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    available_from = models.TimeField()
    available_until = models.TimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        """ returns meal category title"""
        return self.title

    def availability(self):
        return f"served from {self.available_from} - {self.available_until}"


class Meal(models.Model):
    """
    Schema for Meal model
    """
    meal_name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='meals')
    dietary_info = models.TextField(blank=True)
    allergy_info = models.TextField(blank=True)
    price = models.FloatField()
    is_available = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_available', '-category']

    def __str__(self):
        return self.meal_name
