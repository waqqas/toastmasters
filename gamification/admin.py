from django.contrib import admin

from .admin_models import AwardedPointAdmin, PointAdmin
from .models import AwardedPoint, Point

admin.site.register(Point, PointAdmin)
admin.site.register(AwardedPoint, AwardedPointAdmin)
