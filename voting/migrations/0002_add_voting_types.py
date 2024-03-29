# Generated by Django 4.1 on 2023-05-05 05:45

from django.db import migrations

from voting.models import PollType

poll_types = [
    {"name": "Best Prepared Speaker"},
    {
        "name": "Best Table Topic Speaker",
    },
    {
        "name": "Best Evaluator",
    },
    {
        "name": "Best of Big 3",
    },
]


class Migration(migrations.Migration):
    def add_poll_types(app, schema_editor):
        awards = [PollType(**data) for data in poll_types]
        PollType.objects.bulk_create(awards)

    def remove_poll_types(app, schema_editor):
        names = [data["name"] for data in poll_types]
        PollType.objects.filter(name__in=names).delete()

    dependencies = [
        ("voting", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(add_poll_types, remove_poll_types),
    ]
