from django.urls import path
from . import views

urlpatterns = [
    path("get_dishes/", views.GetDieshes.as_view(), name='get_dishes'),
    path("get_nutrition/", views.GetNutrition.as_view(), name='get_nutrition'),
]
