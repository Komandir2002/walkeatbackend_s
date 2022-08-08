from rest_framework import serializers
from .models import User

from django.contrib.auth import authenticate


class UserSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    username = serializers.CharField(max_length=30, min_length=8)
    phone = serializers.CharField(min_length=12, max_length=13)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(min_length=8, max_length=25)

    class Meta:
        model = User
        fields = ["id", "username", "phone", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=30)
    password = serializers.CharField()
