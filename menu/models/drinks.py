from django.db import models


class DrinkCategory(models.Model):
    """
    Drink type model
    """
    DRINK_TYPES = (
        ('AL', 'Alcoholic drink'),
        ('NAL', 'Non-alcoholic drink'),
        ('HOT', 'Hot drink')
    )
    title = models.CharField(max_length=200, unique=True)
    drink_type = models.CharField(
        max_length=3, choices=DRINK_TYPES, default='AL')

    class Meta:
        verbose_name_plural = "drink categories"

    def __str__(self):
        return self.title


class Drink(models.Model):
    """
    Drink model
    """
    drink_name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    drink_category = models.ForeignKey(
        DrinkCategory, on_delete=models.CASCADE, related_name='drinks')
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
