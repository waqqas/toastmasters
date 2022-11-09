from django.contrib import admin
from django.utils.translation import gettext_lazy as _


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


class AwardAdmin(admin.ModelAdmin):
    pass


class AwardedAwardAdmin(admin.ModelAdmin):
    list_filter = ("user",)
