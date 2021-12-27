from rest_framework import serializers

from src.accounts.models import User
from src.api.models import Capture, CaloriesConsumption


class CaptureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capture
        fields = [
            'image', 'user', 'accuracy', 'calories', 'category', 'is_active', 'created_on', 'updated_on'
        ]
        read_only_fields = [
            'user', 'accuracy', 'calories', 'category', 'created_on', 'updated_on'
        ]


class CaloriesConsumptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaloriesConsumption
        fields = [
            'user', 'food_item', 'quantity', 'calories', 'is_active', 'created_on', 'updated_on'
        ]
        read_only_fields = [
            'user', 'updated_on'
        ]


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'phone_number',
        ]


class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'profile_image',
        ]