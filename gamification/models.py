from datetime import datetime, timezone

from dateutil.relativedelta import relativedelta
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.timezone import make_aware

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


class Award(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(default=None, null=True, blank=True)
    user = models.ManyToManyField(User, through="AwardedAward", related_name="awards")

    def __str__(self):
        return f"{self.name}"


class AwardedAward(models.Model):
    award = models.ForeignKey(Award, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.award} awarded to {self.user} in month of {self.award_date.strftime('%b %Y')}"

    # @staticmethod
    # def calculate_award_for_user(user: User):

    #     calculate_start = user.date_joined.award_date()

    #     latest_award = AwardedAward.objects.filter(user=user).order_by("-award_date").first()
    #     if latest_award:
    #         # Calculate for the next month
    #         calculate_start = latest_award.award_date + relativedelta(months=1)

    #     calculate_end = make_aware(datetime.now()).date()

    #     calculate_for_months = []
    #     while calculate_start.year <= calculate_end.year and calculate_start.month <= calculate_end.month:
    #         calculate_for_months.append(calculate_start)
    #         calculate_start += relativedelta(months=1)

    #     print(calculate_for_months)
