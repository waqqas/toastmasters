from django.conf import settings
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


def api_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if not response:
        data = {
            "error": _("Something went wrong") if not settings.DEBUG else str(exc),
        }
        response = Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response
