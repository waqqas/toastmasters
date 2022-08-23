from django.contrib import admin


class PointAdmin(admin.ModelAdmin):
    list_display = ("role", "points")
