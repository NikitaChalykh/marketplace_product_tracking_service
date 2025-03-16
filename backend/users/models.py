from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Adding a required and unique email field
    while keeping the possibility of customizing the user model
    """
    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name="Email"
    )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username


User = get_user_model()
