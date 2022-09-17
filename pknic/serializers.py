from rest_framework import serializers


class LookupSerializer(serializers.Serializer):
    pass


class LookupErrorSerializer(serializers.Serializer):
    pass


class DomainSerializer(serializers.Serializer):
    domain = serializers.CharField(required=True, max_length=50)

    def lookup(self):
        pass
