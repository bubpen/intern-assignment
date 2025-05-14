from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class SignupSerializer(serializers.Serializer):
    username = serializers.CharField()
    nickname = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        if CustomUser.objects.filter(username=data["username"]).exists() or \
           CustomUser.objects.filter(nickname=data["nickname"]).exists():
            raise serializers.ValidationError({
                "error": {
                    "code": "USER_ALREADY_EXISTS",
                    "message": "이미 가입된 사용자입니다."
                }
            })
        return data

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data["username"],
            nickname=validated_data["nickname"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError({
                "error": {
                    "code": "INVALID_CREDENTIALS",
                    "message": "아이디 또는 비밀번호가 올바르지 않습니다."
                }
            })

        refresh = RefreshToken.for_user(user)
        return {
            "token": str(refresh.access_token)  # access token만 반환
        }