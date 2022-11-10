import json

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class PointAdmin(admin.ModelAdmin):
    list_display = (
        "role",
        "points",
    )


class MonthFilter(admin.SimpleListFilter):
    title = _("month")
    parameter_name = "month"

    def lookups(self, request, model_admin):
        return (
            ("1", _("January")),
            ("2", _("February")),
            ("3", _("March")),
            ("4", _("April")),
            ("5", _("May")),
            ("6", _("June")),
            ("7", _("July")),
            ("8", _("August")),
            ("9", _("September")),
            ("10", _("October")),
            ("11", _("November")),
            ("12", _("December")),
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(
                performed__participation__event__held_on__month=self.value()
            )


class YearFilter(admin.SimpleListFilter):
    title = _("year")
    parameter_name = "year"

    def lookups(self, request, model_admin):
        return (
            ("2022", _("2022")),
            ("2023", _("2023")),
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(
                performed__participation__event__held_on__year=self.value()
            )


class AwardedPointAdmin(admin.ModelAdmin):
    list_display = (
        "performed",
        "points",
    )
    list_filter = (
        "user",
        MonthFilter,
        YearFilter,
        "performed__role",
        "performed__participation__event__held_on",
    )

    def changelist_view(self, request, extra_context=None):
        change_list = self.get_changelist_instance(request)

        data = (
            change_list.queryset.values("user")
            .annotate(total_points=Sum("points"))
            .order_by("-total_points")[:10]
        )

        top_users = [
            User.objects.get(pk=user_id) for user_id in [item["user"] for item in data]
        ]
        labels = json.dumps(
            [user.first_name for user in top_users], cls=DjangoJSONEncoder
        )
        points = json.dumps(
            [item["total_points"] for item in data], cls=DjangoJSONEncoder
        )

        extra_context = extra_context or {"labels": labels, "points": points}

        return super().changelist_view(request, extra_context=extra_context)


class AwardAdmin(admin.ModelAdmin):
    pass


class AwardedAwardAdmin(admin.ModelAdmin):
    list_filter = ("user",)
