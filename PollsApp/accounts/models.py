from django.db import models
from django.contrib.auth.models import AbstractUser

from core.models import SafeDeleteAbstractClass

# Create your models here.
class User(AbstractUser, SafeDeleteAbstractClass):
    class TypeUsers(models.TextChoices):
        Employee = 'emp'
        Client = 'cli'

    STATUS_FIELD = 'is_active'

    photo = models.ImageField(upload_to="users/photo-profiles/%Y/%m/%d", null=True)
    birthday = models.DateField(null=True)
    type_user = models.CharField(max_length=3, choices=TypeUsers.choices, null=False, default=TypeUsers.Employee)
