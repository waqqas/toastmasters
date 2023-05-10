from django.contrib import admin

# from django.contrib.auth import get_user_model
# User = get_user_model()


class PollTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)


class PollAdmin(admin.ModelAdmin):
    list_display = ("__str__",)


class VoteAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
