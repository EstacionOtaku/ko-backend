from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from .models import User


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=6, max_length=160)
    username = serializers.CharField(min_length=5, max_length=100)
    password = serializers.CharField(max_length=80, write_only=True)
    password_confirmation = serializers.CharField(
        max_length=80, write_only=True
    )

    def validate_password_confirmation(self, value):
        data = self.get_initial()
        if value != data.get('password'):
            raise serializers.ValidationError("Password don't match")
        return value

    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        return User.objects.create_user(
            **validated_data
        )


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=6, max_length=160)
    password = serializers.CharField(max_length=80, write_only=True)
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])
        tokens = user.tokens()

        return {
            'refresh_token': tokens['refresh_token'],
            'access_token': tokens['access_token']
        }

    def validate(self, values):
        email = values.get('email')
        password = values.get('password')
        user = authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed(
                'User not found or credentials is invalid'
            )

        return values
