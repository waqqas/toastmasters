from django.db import models


class GamificationUser(models.Model):
    last_awards_calculation = models.DateField(default=None, null=True, blank=True)

    class Meta:
        abstract = True
