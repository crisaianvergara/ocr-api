from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import CustomUser


class CustomerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "email",
            "is_superuser",
            "is_staff",
        )


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name", "email", "date_joined", "is_active"]


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "first_name", "last_name", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

        def create(self, validated_data):
            return CustomUser.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect credentials.")
