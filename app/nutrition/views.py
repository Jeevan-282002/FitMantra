from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import helpers


# Create your views here.

class GetDieshes(APIView):
    def post(self, request):
        try:
            return helpers.get_dishes(request)
        except Exception as e:
            return Response({"message": f"Something went wrong: {str(e)}"}, status=500)


class GetNutrition(APIView):
    def post(self, request):
        try:
            return helpers.get_nutrition(request)
        except Exception as e:
            return Response({"message": f"Something went wrong: {str(e)}"}, status=500)
