from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager


class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=150)
    username = None

    is_special = models.BooleanField(default=False)
    limit = models.PositiveSmallIntegerField(default=10,blank=True,null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email