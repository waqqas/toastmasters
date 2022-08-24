# Generated by Django 4.1 on 2022-08-24 12:54
from django.db import migrations

from event.models import Role

role_data = [
    # Basic
    {"name": "Absent"},
    {"name": "Attended Meeting"},
    # Speaker
    {"name": "Prepared Speaker"},
    {"name": "Table Topic Speaker"},
    # TAG roles
    {"name": "Vote Counter"},
    {"name": "Timer"},
    {"name": "Ah Counter"},
    {"name": "Grammarian"},
    # Evaluator
    {"name": "Table Topic Evaluator"},
    {"name": "Prepared Speech Evaluator"},
    # Big 3 roles
    {"name": "Toastmaster of the Evening"},
    {"name": "Table Topic Master"},
    {"name": "General Evaluator"},
    # Best
    {"name": "Best Speaker"},
    {"name": "Best Table Topic"},
    {"name": "Best Evaluator"},
    {"name": "Best of Big 3"},
    # Contest
    {"name": "Contest Speaker"},
    {"name": "Contest Participation"},
    {"name": "Contest Chair"},
]


class Migration(migrations.Migration):
    def add_role_data(apps, schema_editor):
        """Insert initial role data"""
        roles = [Role(**data) for data in role_data]
        Role.objects.bulk_create(roles)

    def remove_role_data(apps, schema_editor):
        """Remove initial role data"""
        role_names = [role["name"] for role in role_data]
        Role.objects.filter(name__in=role_names).delete()

    dependencies = [
        ("event", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(add_role_data, remove_role_data),
    ]
