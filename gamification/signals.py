from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from event.models import PerformedRole

from .models import AwardedPoint


@receiver(post_save, sender=PerformedRole)
def award_points(sender, instance, created, **kwargs):
    awarded_point = AwardedPoint(
        performed=instance,
        points=instance.role.point.points,
        user=instance.participation.user,
    )
    awarded_point.save()


# @receiver(post_delete, sender=PerformedRole)
# def remove_points(sender, instance, **kwargs):
#     AwardedPoint.objects.filter(performed=instance).delete()
