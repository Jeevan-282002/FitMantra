from app.models.meals_models import DailyUserDishes
from rest_framework import serializers
import datetime


class DailyUserDishesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyUserDishes
        fields = '__all__'

    def insert(self, data):
        obj = DailyUserDishes.objects.create(
            user=data.get('user'),
            dish_type=data.get('dish_type'),
            dish_name=data.get('dish_name'),
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
            is_active=True
        )
        if obj:
            return True
