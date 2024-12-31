from rest_framework import serializers
from ..models.account_models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["id", "name", "age", "weight", "height", "user", "created_at", "updated_at", "is_active",]
