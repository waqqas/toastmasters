from django.db import models
from django.utils.translation import gettext_lazy as _


class EventType(models.TextChoices):
    REGULAR_SESSION = "regular_session", _("Regular Session")
    JOINT_SESSION = "joint_session", _("Joint Session")
    CONTEST = "contest", _("Contest")
