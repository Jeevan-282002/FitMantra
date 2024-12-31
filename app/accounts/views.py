from rest_framework.views import APIView
from rest_framework.response import Response
from . import helpers
from rest_framework.permissions import IsAuthenticated


class UserRegistration(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            return helpers.user_registration(request)
        except Exception as e:
            return Response({"message": f"Something went wrong: {str(e)}"}, status=500)


class LoginView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            return helpers.do_login(self, request)
        except Exception as e:
            return Response({"message": f"Something went wrong: {str(e)}"}, status=500)


class GetUserList(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            return helpers.get_user_list(self, request)
        except Exception as e:
            return Response({"message": f"Something went wrong: {str(e)}"}, status=500)


class CalculateBmi(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            return helpers.calculate_bmi(request)
        except Exception as e:
            return Response({"message": f"Something went wrong: {str(e)}"}, status=500)


class GetFreeSearchRoken(APIView):
    def post(self, request):
        try:
            return helpers.get_free_search_token(request)
        except Exception as e:
            return Response({"message": f"Something went wrong: {str(e)}"}, status=500)

