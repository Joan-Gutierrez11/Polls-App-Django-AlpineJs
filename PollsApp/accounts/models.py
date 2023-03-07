from django.db import models
from django.contrib.auth.models import AbstractUser

from core.models import SafeDeleteAbstractClass

# Create your models here.
class User(AbstractUser, SafeDeleteAbstractClass):
    STATUS_FIELD = 'is_active'

    photo = models.ImageField(null=True)