from django.contrib import admin


class EventAdmin(admin.ModelAdmin):
    list_display = ("type", "held_on")
