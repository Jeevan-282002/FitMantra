from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegistration.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('get_user_list/', views.GetUserList.as_view(), name='get_user_list'),
    path('calculate_bmi/', views.CalculateBmi.as_view(), name='calculate_bmi'),
    path('get_free_search_token/', views.GetFreeSearchRoken.as_view(), name='get_free_search_token')
]
