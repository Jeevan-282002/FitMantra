from django.contrib.auth.models import User
from app.models.account_models import UserProfile


def get_user_details(self, request):
    user_obj = User.objects.get(username=request.user)
    user_prof_obj = UserProfile.objects.filter(user_id=user_obj.id).first()
    return user_obj, user_prof_obj,  request.data
