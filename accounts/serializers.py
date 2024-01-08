from rest_framework import serializers
from django.forms import ValidationError
from .models import Account
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["id", "username", "password", "email", "is_superuser"]
        extra_kwargs = {
            "id": {"read_only": True},
            "is_superuser": {"required": False},
            "password": {"write_only": True},
            "username": {"validators": []},
        }

    def validate_username(self, req_username):
        if Account.objects.filter(username=req_username).first():
            raise ValidationError("A user with that username already exists.", code=400)
        return req_username

    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)


# SOBRESCREVER MÉTODOS DO TOKEN: ADD ATRIBUTOS PARA APARECER NO TOKEN
class CustomJWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Também aparecerá o is_superuser
        token["is_superuser"] = user.is_superuser
        return token
