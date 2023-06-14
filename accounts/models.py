from django.contrib.auth.models import AbstractUser
from django.db import models

from gamification.mixins import GamificationUser


class User(AbstractUser, GamificationUser):
    """User model"""

    # safe_fields = ["username", "first_name", "last_name", "email"]

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return self.first_name
        else:
            return self.username
