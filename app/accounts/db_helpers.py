from ..models.account_models import User, UserProfile
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import json
import requests


def get_auth_token(username, password):
    try:
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {
            'grant_type': 'password',
            'username': username,
            'password': password,
            'client_id': settings.CLIENT_ID,
            'client_secret': settings.CLIENT_SECRET
        }
        url = 'http://127.0.0.1:8000/oauth/token/'
        api_response = requests.post(
            url=url,
            data=payload,
            headers=headers
        )
        if api_response.ok:
            return json.loads(api_response.text)
    except Exception as ex:
        return None


def check_user_exists(username):
    try:
        if User.objects.filter(username=username).exists():
            return True
        else:
            return False
    except Exception as ex:
        return None


def get_user_list_helper(request):
    try:
        kwargs = {}
        user = request.data.get('user', None)
        age = request.data.get('age', None)
        weight = request.data.get('weight', None)
        height = request.data.get('height', None)
        limit = request.data.get('limit', 10)
        offset = request.data.get('offset', 0)

        if user:
            kwargs["user__username"] = user
        if age:
            kwargs["age"] = age
        if weight:
            kwargs["weight"] = weight
        if height:
            kwargs["height"] = height
        user_list = UserProfile.objects.filter(**kwargs)[offset:offset + limit]
        count = user_list.count()
        return user_list, count
    except Exception as e:
        return None
