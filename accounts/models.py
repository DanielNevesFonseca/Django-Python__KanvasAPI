from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class Account(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=150, unique=True, null=False)
    password = models.CharField(max_length=128, null=False)
    email = models.CharField(max_length=100, unique=True, null=False)
    is_superuser = models.BooleanField(default=False)
