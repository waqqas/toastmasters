from django.db import models


class Point(models.Model):
    role = models.CharField(max_length=64, default="", unique=True)
    points = models.IntegerField(default=0)
