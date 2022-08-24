from django.contrib import admin


class EventAdmin(admin.ModelAdmin):
    list_display = ("type", "held_on")


class RoleAdmin(admin.ModelAdmin):
    list_display = ("name",)


class ParticipationAdmin(admin.ModelAdmin):
    list_filter = ("user",)


class PerformedRoleAdmin(admin.ModelAdmin):
    list_filter = (
        "participation__user",
        "role__name",
    )
