from django.db import models
from django.contrib.auth.models import AbstractUser, User
import datetime


class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    weight =  models.FloatField()
    height = models.FloatField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default = True)

    class Meta:
        db_table = 'user_profile'

    def __str__(self):
        return self.name