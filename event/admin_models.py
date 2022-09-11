from nested_admin import NestedInlineModelAdmin as InlineModelAdmin
from nested_admin import NestedModelAdmin as ModelAdmin
from nested_admin import NestedStackedInline as StackedInline
from nested_admin import NestedTabularInline as TabularInline

from event.models import Participation, PerformedRole
from toastmasters.mixins import ExportCsvMixin


class PerformedRoleInline(TabularInline):
    model = PerformedRole
    extra = 5


class ParticipationInline(StackedInline):
    model = Participation
    extra = 5
    inlines = (PerformedRoleInline,)


class EventAdmin(ModelAdmin, ExportCsvMixin):
    list_display = (
        "type",
        "held_on",
    )
    list_filter = (
        "type",
        "held_on",
    )
    inlines = (ParticipationInline,)
    ordering = ("-held_on",)


class RoleAdmin(ModelAdmin):
    list_display = ("name",)


class ParticipationAdmin(ModelAdmin, ExportCsvMixin):
    list_filter = ("user", "event__held_on", "event__type")
    inlines = (PerformedRoleInline,)
    actions = ["export_as_csv"]


class PerformedRoleAdmin(ModelAdmin, ExportCsvMixin):
    list_filter = (
        "participation__user",
        "participation__event__held_on",
        "participation__event__type",
        "role__name",
    )
    actions = ["export_as_csv"]
