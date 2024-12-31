from django.db import models
from ..models.account_models import UserProfile


class DailyUserDishes(models.Model):
    BREAKFAST = 'BreakFast'
    LUNCH = 'Lunch'
    DINNER = 'Dinner'
    DISH_TYPE_CHOICES = [
        (BREAKFAST, 'BreakFast'),
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner')]
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    dish_type = models.CharField(max_length=50, choices=DISH_TYPE_CHOICES)
    dish_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField()
