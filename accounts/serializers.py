from rest_framework import serializers
from django.forms import ValidationError
from .models import Account


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
