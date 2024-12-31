from django.urls import path
from . import views

urlpatterns = [
    path("add_daily_food/", views.AddDailyFood.as_view(), name='add_daily_food'),
    path("get_daily_food_list/", views.GetDailyFoodList.as_view(), name='get_daily_food_list'),
]
