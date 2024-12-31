from django.contrib.auth.hashers import make_password
from app.utils import constants
from rest_framework.response import Response
from django.db import transaction
from app.utils import response_translators
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
import requests
from . serializers import DailyUserDishesSerializer
from app.utils import commons
from app.models.meals_models import DailyUserDishes
from . import db_helpers


def add_daily_food(self, request):
    try:
        user_obj, user_prof_obj, request_data = commons.get_user_details(self, request)
        dish_type = request.data.get('dish_type', None)
        dish_name = request.data.get('dish_name', None)

        data = {
            'user': user_prof_obj,
            'dish_type': dish_type,
            'dish_name': dish_name
        }
        serializer = DailyUserDishesSerializer.insert(self, data=data)
        if serializer:
            translator_response = response_translators.basic_response_translator(
                is_success=True, data=constants.DATA_ADDED
            )
            return response_translators.basic_response(message=translator_response, status=200)

    except Exception as e:
        print(f"Error during add daily food: {e}")
        return Response({"message": "Something went wrong", "status": 500}, status=500)


def get_daily_food_list(self, request):
    try:
        user_obj, user_prof_obj, request_data = commons.get_user_details(self, request)

        filter_args = {
            'user': user_prof_obj,
            'dish_name': request.data.get('dish_name', None),
            'dish_type': request.data.get('dish_type', None),
            'offset': int(request.data.get('offset', 0)),
            'limit': int(request.data.get('limit', 10)),
        }
        daily_dish_records, total_count = db_helpers.get_daily_user_dishes(filter_args)
        if not daily_dish_records:
            return response_translators.basic_response(message=constants.DATA_NOT_FOUND, status=200)
        serialized_data = DailyUserDishesSerializer(daily_dish_records, many=True).data
        if serialized_data:
            translator_response = response_translators.basic_response_translator(
                is_success=True,
                data={
                    'total_count': total_count,
                    'results': serialized_data
                }
            )
            return response_translators.basic_response(message=translator_response, status=200)

    except Exception as e:
        print(f"Error during get daily food list: {e}")
        return Response({"message": "Something went wrong", "status": 500}, status=500)

