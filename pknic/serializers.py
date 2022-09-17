import enum

import requests
from bs4 import BeautifulSoup
from dateutil.parser import parse
from rest_framework import serializers


class LookupSerializer(serializers.Serializer):
    domain = serializers.CharField(required=True, max_length=50)
    registered = serializers.BooleanField(required=False)
    created = serializers.DateField(required=False)
    expiry = serializers.DateField(required=False)
    name_servers = serializers.ListField(
        required=False, child=serializers.CharField(required=True, max_length=100)
    )


class LookupPageParserState(str, enum.Enum):
    START = "START"
    DOMAIN_NAME_KEY = "DOMAIN_NAME_KEY"
    DOMAIN_NAME_VALUE = "DOMAIN_NAME_VALUE"
    DOMAIN_REG_STATUS = "DOMAIN_REG_STATUS"
    CREATE_DATE_KEY = "CREATE_DATE_KEY"
    CREATE_DATE_VALUE = "CREATE_DATE_VALUE"
    EXPIRY_DATE_KEY = "EXPIRY_DATE_KEY"
    EXPIRY_DATE_VALUE = "EXPIRY_DATE_VALUE"
    DNS_NAMESERVERS_KEY = "DNS_NAMESERVERS_KEY"
    DNS_NAMESERVERS_VALUE = "DNS_NAMESERVERS_VALUE"
    COMPLETE = "COMPLETE"
    DOMAIN_NOT_FOUND_KEY = "DOMAIN_NOT_FOUND_KEY"
    DOMAIN_NOT_FOUND_VALUE = "DOMAIN_NOT_FOUND"


class DomainSerializer(serializers.Serializer):
    domain = serializers.CharField(required=True, max_length=50)

    def _get_page_data(self, page) -> dict:
        state: LookupPageParserState = LookupPageParserState.START
        response = {}

        table = page.find("table", border="0", width="707")
        if table:
            state = LookupPageParserState.DOMAIN_NAME_KEY
            for data in table.stripped_strings:
                if (
                    state == LookupPageParserState.DOMAIN_NAME_KEY
                    and data == "Domain Name"
                ):
                    state = LookupPageParserState.DOMAIN_NAME_VALUE
                elif state == LookupPageParserState.DOMAIN_NAME_VALUE:
                    response["domain"] = data
                    state = LookupPageParserState.DOMAIN_REG_STATUS
                elif state == LookupPageParserState.DOMAIN_REG_STATUS:
                    if data == "Domain is Registered":
                        response["registered"] = True
                    else:
                        response["registered"] = False
                    state = LookupPageParserState.CREATE_DATE_KEY
                elif (
                    state == LookupPageParserState.CREATE_DATE_KEY
                    and data == "Create Date:"
                ):
                    state = LookupPageParserState.CREATE_DATE_VALUE
                elif state == LookupPageParserState.CREATE_DATE_VALUE:
                    response["created"] = parse(data).date()
                    state = LookupPageParserState.EXPIRY_DATE_KEY
                elif (
                    state == LookupPageParserState.EXPIRY_DATE_KEY
                    and data == "Expire Date:"
                ):
                    state = LookupPageParserState.EXPIRY_DATE_VALUE
                elif state == LookupPageParserState.EXPIRY_DATE_VALUE:
                    response["expiry"] = parse(data).date()
                    state = LookupPageParserState.DNS_NAMESERVERS_KEY
                elif (
                    state == LookupPageParserState.DNS_NAMESERVERS_KEY
                    and data == "DNS Nameservers"
                ):
                    response["name_servers"] = []
                    state = state = LookupPageParserState.DNS_NAMESERVERS_VALUE
                elif state == LookupPageParserState.DNS_NAMESERVERS_VALUE:
                    if data != "None Specified (or deleted)":
                        response["name_servers"].append(data)
                    else:
                        state = LookupPageParserState.COMPLETE
        else:
            response["registered"] = False

            state = LookupPageParserState.DOMAIN_NOT_FOUND_KEY
            for data in page.stripped_strings:
                if (
                    state == LookupPageParserState.DOMAIN_NOT_FOUND_KEY
                    and data == "Domain not found:"
                ):
                    state = LookupPageParserState.DOMAIN_NOT_FOUND_VALUE
                elif state == LookupPageParserState.DOMAIN_NOT_FOUND_VALUE:
                    response["domain"] = data
                    state = LookupPageParserState.COMPLETE

        return response

    def lookup(self):
        response = requests.post(
            url="https://pk6.pknic.net.pk/pk5/lookup.PK",
            data={"name": self.validated_data["domain"]},
        )

        response.raise_for_status()

        page = BeautifulSoup(response.text, "lxml")
        return self._get_page_data(page)
