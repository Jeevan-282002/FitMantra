from ..models.account_models import User, UserProfile
from .serializers import UserProfileSerializer
from django.contrib.auth.hashers import make_password
from . import db_helpers
from rest_framework.response import Response
from django.db import transaction
from app.utils import response_translators
from app.utils import constants
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from FitMantra import settings


def user_registration(request):
    try:
        name = request.data.get("first_name", "").strip() + " " + request.data.get("last_name", "").strip()
        username = request.data.get("username", "").strip()
        password = request.data.get("password", "").strip()
        age = request.data.get("age", "").strip()
        weight = request.data.get("weight", "").strip()
        height = request.data.get("height", "").strip()

        user_exists = User.objects.filter(username=username).exists()
        if user_exists:
            return response_translators.basic_response(message=constants.USER_EXISTS,
                                                       status=200)

        user = User(
            username=username,
            email=request.data.get("email", "").strip(),
            first_name=request.data.get("first_name", "").strip(),
            last_name=request.data.get("last_name", "").strip(),
            password=make_password(password),
        )
        user.save()
        profile_data = {
            "user": user.id,
            "name": name,
            "age": age,
            "weight": weight,
            "height": height,
        }
        serializer = UserProfileSerializer(data=profile_data)
        if serializer.is_valid():
            serializer.save()
            db_user_info = serializer.data
            translator_response = response_translators.basic_response_translator(
                is_success=True, data=db_user_info
            )
            return response_translators.basic_response(message=translator_response, status=200)
        else:
            return response_translators.basic_response(message=constants.VALIDATION_FAILED,
                                                       status=200)

    except Exception as e:
        print(f"Error during user registration: {e}")
        return Response({"message": "Something went wrong", "status": 500}, status=500)


def do_login(self, request):
    try:
        username = request.data.get('username',None)
        password = request.data.get('password',None)
        if not username and password:
            return response_translators.basic_response(message=constants.INVALID_REQUEST,
                                                       status=200)
        user = authenticate(username=username, password=password)
        if not user:
            return response_translators.basic_response(message=constants.DATA_NOT_FOUND,
                                                       status=200)
        user_profile_obj = UserProfile.objects.get(user=user)
        if not user_profile_obj.is_active:
            return response_translators.basic_response(message=constants.INACTIVE_USER,
                                                       status=200)
        token = db_helpers.get_auth_token(username, password)
        if not token:
            return response_translators.basic_response(message=constants.DATA_NOT_FOUND,
                                                       status=200)
        serializer = UserProfileSerializer(user_profile_obj).data
        serializer['token'] = token
        if token:
            translator_response = response_translators.basic_response_translator(
                is_success=True, data=serializer
            )
            return response_translators.basic_response(message=translator_response, status=200)
    except Exception as ex:
        return response_translators.main_exception(
            error_message=constants.SOMETHING_WENT_WRONG,
            status=500
        )


def get_user_list(self, request):
    try:
        records, count = db_helpers.get_user_list_helper(request)
        if not records:
            return response_translators.basic_response(message=constants.DATA_NOT_FOUND,
                                                       status=200)
        serialized_data = UserProfileSerializer(records, many=True).data
        if not serialized_data:
            return response_translators.basic_response(message=constants.DATA_NOT_FOUND,
                                                       status=200)
        translator_response = response_translators.basic_response_translator(
            is_success=True, data=serialized_data,
            total_result=count
        )
        return response_translators.basic_response(translator_response, status=200)
    except Exception as e:
        return response_translators.main_exception(
            error_message=constants.SOMETHING_WENT_WRONG,
            status=500
        )


def calculate_bmi(request):
    try:
        user_id = request.data.get("user_id", "")
        userprofile_obj = UserProfile.objects.filter(id=user_id).first()
        if not userprofile_obj:
            return response_translators.basic_response(message=constants.DATA_NOT_FOUND,
                                                       status=200)
        weight = userprofile_obj.weight
        height = userprofile_obj.height
        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"
        data = {"bmi": bmi, "category": category}
        translator_response = response_translators.basic_response_translator(
            is_success=True, data=data
        )
        return response_translators.basic_response(translator_response, status=200)
    except Exception as e:
        return response_translators.main_exception(
            error_message=constants.SOMETHING_WENT_WRONG,
            status=500
        )


def get_free_search_token(request):
    try:
        guest_username = settings.GUEST_USERNAME
        guest_password = settings.GUEST_PASSWORD
        token = db_helpers.get_auth_token(guest_username, guest_password)
        if not token:
            return response_translators.basic_response(message=constants.DATA_NOT_FOUND,
                                                       status=200)
        translator_response = response_translators.basic_response_translator(
            is_success=True, data=token
        )
        return response_translators.basic_response(translator_response, status=200)
    except Exception as e:
        return response_translators.main_exception(
            error_message=constants.SOMETHING_WENT_WRONG,
            status=500
        )