"""Methods for GamificationUser"""
from datetime import date, datetime
from typing import List

from dateutil.relativedelta import relativedelta
from django.db.models import Count, F, Q, When
from django.db.models.lookups import GreaterThan, LessThan
from django.utils.timezone import make_aware

from event.models import PerformedRole

from .date import start_of_month
from .mixins import GamificationUser
from .models import Award, AwardedAward


def get_awards_calculation_months(self) -> List[date]:
    """Get a list of months for which awards need to be calculated

    Day is always 1st of each month
    """
    calculate_start = self.last_awards_calculation
    if not calculate_start:
        calculate_start = self.date_joined.date()
    calculate_start = start_of_month(calculate_start)

    calculate_end = make_aware(datetime.now()).date()
    calculate_end = start_of_month(calculate_end)

    calculate_for_months = []

    while calculate_start <= calculate_end:
        calculate_for_months.append(calculate_start)
        calculate_start += relativedelta(months=1)
    return calculate_for_months


def calculate_awards(self):
    """Calculate awards for the user"""
    calculate_for_months = self.get_awards_calculation_months()
    for award_date in calculate_for_months:
        awards = [
            award
            for award in Award.objects.all()
            if self.is_eligible(award, award_date)
        ]
        awarded_awards = [AwardedAward(user=self, award=award) for award in awards]
        for awarded_award in awarded_awards:
            awarded_award.save()
    if calculate_for_months:
        self.last_awards_calculation = calculate_for_months[-1]
        self.save()


def is_eligible(self, award: Award, award_date: date):
    """Check if a user is eligible for the award for a give month"""
    eligible = False
    start_date = start_of_month(award_date)
    end_date = start_of_month(award_date + relativedelta(months=1))
    if award.name == "Been there, Done that":
        eligible = PerformedRole.objects.filter(
            Q(role__name="Table Topic Master")
            & Q(role__name="General Evaluator")
            & Q(role__name="Table Topic Evaluator")
            & (
                Q(role__name="Timer")
                | Q(role__name="Vote Counter")
                | Q(role__name="Ah Counter")
                | Q(role__name="Grammarian")
            ),
            participation__user=self,
            participation__event__held_on__gte=start_date,
            participation__event__held_on__lt=end_date,
        ).exists()
    elif award.name == "You Need Me":
        eligible = PerformedRole.objects.filter(
            Q(role__name="Speech Evaluator")
            & Q(role__name="Table Topic Evaluator")
            & (
                Q(role__name="Toastmaster of the Evening")
                | Q(role__name="General Evaluator")
                | Q(role__name="Table Topic Master")
            ),
            participation__user=self,
            participation__event__held_on__gte=start_date,
            participation__event__held_on__lt=end_date,
        ).exists()
    elif award.name == "You Need Me":
        eligible = PerformedRole.objects.filter(
            Q(role__name="Speech Evaluator")
            & Q(role__name="Table Topic Evaluator")
            & (
                Q(role__name="Toastmaster of the Evening")
                | Q(role__name="General Evaluator")
                | Q(role__name="Table Topic Master")
            ),
            participation__user=self,
            participation__event__held_on__gte=start_date,
            participation__event__held_on__lt=end_date,
        ).exists()
    elif award.name == "I am Everywhere":
        eligible = (
            PerformedRole.objects.filter(
                Q(role__name="Attended Meeting"),
                participation__user=self,
                participation__event__held_on__gte=start_date,
                participation__event__held_on__lt=end_date,
            ).count()
            >= 4
        )

    return eligible


setattr(
    GamificationUser,
    get_awards_calculation_months.__name__,
    get_awards_calculation_months,
)
setattr(GamificationUser, calculate_awards.__name__, calculate_awards)
setattr(GamificationUser, is_eligible.__name__, is_eligible)
