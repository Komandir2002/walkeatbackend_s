from rest_framework import serializers
from .models import User

from django.contrib.auth import authenticate


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = ["email", "username", "phone","password", "password2"]

    def save(self, *args, **kwargs):
        user = User(
            email=self.validated_data["email"],
            username=self.validated_data["username"],
            phone=self.validated_data["phone"]
        )
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]
        if password != password2:
            raise serializers.ValidationError({password: "Пароль не совпадает"})
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, read_only=True, required=False)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)

        if password is None:
            raise serializers.ValidationError("A password is required to log in.")

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError("A user was not found.")

        if not user.is_active:
            raise serializers.ValidationError("This user has been deactivated.")
        return {
            "username": user.phone,
            "token": user.token,
        }
