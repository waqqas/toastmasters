from django.db import models

# from django.conf import settings
# from django.apps import apps

# def get_gamification_user_model():
#     """
#     Return the Gamification User model that is active in this project.
#     """
#     try:
#         return apps.get_model(settings.GAMIFICATION_USER_MODEL, require_ready=False)
#     except ValueError:
#         raise ImproperlyConfigured(
#             "GAMIFICATION_USER_MODEL must be of the form 'app_label.model_name'"
#         )
#     except LookupError:
#         raise ImproperlyConfigured(
#             "GAMIFICATION_USER_MODEL refers to model '%s' that has not been installed"
#             % settings.AUTH_USER_MODEL
#         )


class GamificationUser(models.Model):
    last_awards_calculation = models.DateField(default=None, null=True, blank=True)

    class Meta:
        abstract = True
