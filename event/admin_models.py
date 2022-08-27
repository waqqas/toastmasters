from django.contrib import admin

from event.models import Participation, PerformedRole


class ParticipationInline(admin.TabularInline):
    model = Participation


class EventAdmin(admin.ModelAdmin):
    list_display = ("type", "held_on")
    inlines = (ParticipationInline,)


class RoleAdmin(admin.ModelAdmin):
    list_display = ("name",)


class PerformedRoleInline(admin.TabularInline):
    model = PerformedRole


class ParticipationAdmin(admin.ModelAdmin):
    list_filter = ("user",)
    inlines = (PerformedRoleInline,)


class PerformedRoleAdmin(admin.ModelAdmin):
    list_filter = (
        "participation__user",
        "role__name",
    )