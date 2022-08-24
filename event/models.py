from django.contrib.auth import get_user_model
from django.db import models

from .enums import EventType

User = get_user_model()


class Event(models.Model):
    """An event related to toastmasters"""

    type = models.CharField(max_length=64, choices=EventType.choices)
    held_on = models.DateField()

    # relations
    users = models.ManyToManyField(
        User,
        through="Participation",
        related_name="events",
    )

    def __str__(self):
        return f"{EventType(self.type).label} on {self.held_on}"


class Role(models.Model):
    """Role a person can perform in an event"""

    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class PerformedRole(models.Model):
    """Role performed by a person while participating in an event"""

    participation = models.ForeignKey("Participation", on_delete=models.CASCADE)

    role = models.OneToOneField(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.participation} as {self.role}"


class Participation(models.Model):
    """Participation in a meeting"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} participated in a {self.event}"

    # relations
    roles = models.ManyToManyField(
        Role,
        through=PerformedRole,
    )
