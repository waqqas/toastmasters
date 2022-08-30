from django.contrib import admin

from event.models import Participation, PerformedRole


class ParticipationInline(admin.TabularInline):
    model = Participation
    extra = 20


class EventAdmin(admin.ModelAdmin):
    list_display = (
        "type",
        "held_on",
    )
    list_filter = (
        "type",
        "held_on",
    )
    inlines = (ParticipationInline,)


class RoleAdmin(admin.ModelAdmin):
    list_display = ("name",)


class PerformedRoleInline(admin.TabularInline):
    model = PerformedRole


class ParticipationAdmin(admin.ModelAdmin):
    list_filter = ("user", "event__held_on", "event__type")
    inlines = (PerformedRoleInline,)


class PerformedRoleAdmin(admin.ModelAdmin):
    list_filter = (
        "participation__user",
        "participation__event__held_on",
        "participation__event__type",
        "role__name",
    )
