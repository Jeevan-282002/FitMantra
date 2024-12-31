from django.contrib import admin
from .models.account_models import *
from .models.meals_models import *
from .models.nutrition_models import *

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(DailyUserDishes)