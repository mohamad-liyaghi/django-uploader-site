from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_special = models.BooleanField(default=False)
    limit = models.PositiveSmallIntegerField(default=10,blank=True,null=True)