from django.db import models

from .enums import EventType


class Event(models.Model):
    type = models.CharField(max_length=64, choices=EventType.choices)
    held_on = models.DateField()
