from django.contrib.auth import get_user_model
from django.db import models

from event.models import PerformedRole, Role

User = get_user_model()


class Point(models.Model):
    role = models.OneToOneField(Role, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.role}({self.points})"


class AwardedPoint(models.Model):
    points = models.IntegerField(default=0)

    # relations
    performed = models.ForeignKey(PerformedRole, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.performed.role}({self.points})"
