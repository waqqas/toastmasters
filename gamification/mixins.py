from datetime import date, datetime
from typing import List

from django.db import models
from django.utils.timezone import make_aware


class GamificationUser(models.Model):
    last_awards_calculation = models.DateField(default=None, null=True, blank=True)

    class Meta:
        abstract = True

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
