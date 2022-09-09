from datetime import date, datetime
from typing import List

from dateutil.relativedelta import relativedelta
from django.utils.timezone import make_aware

from .mixins import GamificationUser
from .models import Award, AwardedAward


def get_awards_calculation_months(self) -> List[date]:
    calculate_start = self.last_awards_calculation
    if not calculate_start:
        calculate_start = self.date_joined.date()
    calculate_start = calculate_start.replace(day=1)

    calculate_end = make_aware(datetime.now()).date()
    calculate_end = calculate_end.replace(day=1)

    calculate_for_months = []

    while calculate_start < calculate_end:
        calculate_for_months.append(calculate_start)
        calculate_start += relativedelta(months=1)
    return calculate_for_months


def calculate_awards(self):
    for award_date in self.get_awards_calculation_months():
        awards = [
            award
            for award in Award.objects.all()
            if self.is_eligible(award, award_date)
        ]
        awarded_awards = [AwardedAward(user=self, award=award) for award in awards]
        for awarded_award in awarded_awards:
            awarded_award.save()


def is_eligible(self, award: Award, award_date: date):
    return False


setattr(
    GamificationUser,
    get_awards_calculation_months.__name__,
    get_awards_calculation_months,
)
setattr(GamificationUser, calculate_awards.__name__, calculate_awards)
setattr(GamificationUser, is_eligible.__name__, is_eligible)
