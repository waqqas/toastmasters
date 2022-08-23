from django.contrib import admin

from .admin_models import EventAdmin
from .models import Event

admin.site.register(Event, EventAdmin)
