from django.contrib import admin

from .admin_models import PointAdmin
from .models import Point

admin.site.register(Point, PointAdmin)
