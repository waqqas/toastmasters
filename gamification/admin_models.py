from django.contrib import admin


class PointAdmin(admin.ModelAdmin):
    list_display = (
        "role",
        "points",
    )


class AwardedPointAdmin(admin.ModelAdmin):
    list_display = (
        "performed",
        "points",
    )
    list_filter = (
        "user",
        "performed__role",
        "performed__participation__event__held_on",
    )


class AwardAdmin(admin.ModelAdmin):
    pass
