from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from pknic.serializers import DomainSerializer, LookupSerializer


@api_view(("GET",))
@renderer_classes((JSONRenderer,))
def lookup_domain(request, domain):
    serializer = DomainSerializer(data={"domain": domain})
    serializer.is_valid(raise_exception=True)
    lookup_data = serializer.lookup()
    return Response(LookupSerializer(lookup_data).data, status=status.HTTP_200_OK)
