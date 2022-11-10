from django.core.management.base import BaseCommand
from rest_framework_api_key.models import APIKey


class Command(BaseCommand):
    help = "ModelApi API key management"

    def add_arguments(self, parser):
        parser.add_argument("--service_name", type=str, help="Name of the API key")
        parser.add_argument(
            "command",
            default=None,
            type=str,
            help="Command to execute. Possible options are 'create'",
        )

    def handle(self, *args, **options):
        command = options["command"]

        if command == "create":
            self._create_key(*args, **options)
        else:
            self.stderr.write(self.style.ERROR(f"Invalid command: {command}"))

    def _create_key(self, *args, **options):
        service_name = options.get("service_name")

        if not service_name:
            self.stderr.write(self.style.ERROR("service_name parameter missing"))
            return

        api_key, key = APIKey.objects.create_key(name=service_name)

        self.stdout.write(self.style.SUCCESS(f"{api_key} = {key}"))
