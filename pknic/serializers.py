import requests
from bs4 import BeautifulSoup
from rest_framework import serializers


class LookupSerializer(serializers.Serializer):
    domain = serializers.CharField(required=True, max_length=50)


class LookupErrorSerializer(serializers.Serializer):
    pass


class DomainSerializer(serializers.Serializer):
    domain = serializers.CharField(required=True, max_length=50)

    def lookup(self):
        response = requests.post(
            url="https://pk6.pknic.net.pk/pk5/lookup.PK",
            data=f"name={self.validated_data['domain']}",
        )

        response.raise_for_status()

        page = BeautifulSoup(response.text, "lxml")

        return {"domain": self.validated_data["domain"]}
