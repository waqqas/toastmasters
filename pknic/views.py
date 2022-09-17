from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from pknic.serializers import DomainSerializer, LookupErrorSerializer, LookupSerializer


@api_view(("GET",))
@renderer_classes((JSONRenderer,))
def lookup_domain(request, domain):
    serializer = DomainSerializer(data={"domain": domain})
    if serializer.is_valid():
        serializer.lookup()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(
        LookupErrorSerializer(serializer.errors), status=status.HTTP_400_BAD_REQUEST
    )
