from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import helpers
from app.utils import commons
from rest_framework.permissions import IsAuthenticated


class AddDailyFood(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            return helpers.add_daily_food(self, request)
        except Exception as e:
            return Response({"message": f"Something went wrong: {str(e)}"}, status=500)


class GetDailyFoodList(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            return helpers.get_daily_food_list(self, request)
        except Exception as e:
            return Response({"message": f"Something went wrong: {str(e)}"}, status=500)