from django.contrib import admin

from .admin_models import AwardAdmin, AwardedPointAdmin, PointAdmin
from .models import Award, AwardedPoint, Point

admin.site.register(Point, PointAdmin)
admin.site.register(AwardedPoint, AwardedPointAdmin)
admin.site.register(Award, AwardAdmin)
