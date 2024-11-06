from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinLengthValidator

from users.managers import CustomUserManager


# Create your models here.
class CustomUser(AbstractUser):
    """модель для кастомного пользователя"""

    username = None
    phone_number = models.CharField(max_length=20, validators=[MinLengthValidator(6)], unique=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'