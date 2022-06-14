from django.test import TestCase
from .models import MealCategory, Meal, DrinkCategory, Drink


class TestMealCategoryModel(TestCase):
    """
    Test Meal Category model
    """
    def test_meal_category_string_method_returns_title(self):
        meal_category = MealCategory.objects.create(
             title='lunch',
             available_from='12:00',
             available_until='17:00'
        )
        self.assertEqual(str(meal_category), 'lunch')


class TestMealModel(TestCase):
    """
    Test meal model
    """
    def test_meal_string_returns_meal_name(self):
        meal_category = MealCategory.objects.create(
             title='lunch',
             available_from='12:00',
             available_until='17:00'
        )
        meal = Meal.objects.create(
            meal_name='fried rice',
            description='fried rice',
            meal_category=meal_category,
            price='5.99'
        )
        self.assertEqual(str(meal), 'fried rice')
    

class SetUpDrinkModelTestCase(TestCase):
    """
    setup model for drinks category
    """
    def setUp(self):
        self.drink_title = 'red wine'
        self.drink_category = DrinkCategory.objects.create(
            title=self.drink_title,
            description='wine'
        )


class DrinkCategoryTestCase(SetUpDrinkModelTestCase):
    """
    test drink category model
    """
    def test_drink_category_str_returns_title(self):
        self.assertEqual(str(self.drink_category), self.drink_title)

 
class DrinkTestCase(SetUpDrinkModelTestCase):
    """test drink model"""
    def test_drink_str_returns_drink_name(self):
        self.drink = Drink.objects.create(
            drink_name='seculo mencia',
            description='alcoholic beverage',
            drink_category=self.drink_category,
            price='5.15'
        )
        self.assertEqual(str(self.drink), 'seculo mencia')
