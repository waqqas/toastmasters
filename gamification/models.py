from django.db import models

from event.models import Role


class Point(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.role}({self.points})"
