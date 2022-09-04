from django.contrib import admin

from .admin_models import AwardAdmin, AwardedAwardAdmin, AwardedPointAdmin, PointAdmin
from .models import Award, AwardedAward, AwardedPoint, Point

admin.site.register(Point, PointAdmin)
admin.site.register(AwardedPoint, AwardedPointAdmin)
admin.site.register(Award, AwardAdmin)
admin.site.register(AwardedAward, AwardedAwardAdmin)
