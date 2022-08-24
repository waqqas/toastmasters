from django.contrib import admin

from .admin_models import EventAdmin, ParticipationAdmin, PerformedRoleAdmin, RoleAdmin
from .models import Event, Participation, PerformedRole, Role

admin.site.register(Event, EventAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Participation, ParticipationAdmin)
admin.site.register(PerformedRole, PerformedRoleAdmin)
