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
from . import commons


def get_dishes(request):
    try:
        food_name = request.data.get('food_name', None)
        offset = request.data.get('offset', 0)
        limit = request.data.get('limit', 10)
        if not food_name:
            return response_translators.basic_response(message=constants.INVALID_REQUEST,
                                                       status=200)
        # 3rd party api
        data = commons.get_nutrition_api(request)
        if not data:
            return response_translators.basic_response(message=constants.DATA_NOT_FOUND,
                                                       status=200)
        hits = data["hits"]
        ls = []
        for record in hits:
            recipe = record['recipe']
            ls.append(recipe['label'])

        translator_response = response_translators.basic_response_translator(
            is_success=True, data=ls
        )
        return response_translators.basic_response(message=translator_response, status=200)

    except Exception as e:
        print(f"Error during user registration: {e}")
        return Response({"message": "Something went wrong", "status": 500}, status=500)


def get_nutrition(request):
    try:
        food_name = request.data.get('food_name', None)
        if not food_name:
            return response_translators.basic_response(message=constants.INVALID_REQUEST,
                                                       status=200)
        # 3rd party api
        data = commons.get_nutrition_api(request)
        print(data)
        hits = data["hits"]
        ls = []
        for record in hits:
            recipe = record['recipe']
            ls.append(recipe['totalNutrients'])
        translator_response = response_translators.basic_response_translator(
            is_success=True, data=ls
        )
        return response_translators.basic_response(message=translator_response, status=200)
    except Exception as e:
        print(f"Error during user registration: {e}")
        return Response({"message": "Something went wrong", "status": 500}, status=500)




