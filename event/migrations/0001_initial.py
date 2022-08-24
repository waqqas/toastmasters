# Generated by Django 4.1 on 2022-08-24 12:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("regular_session", "Regular Session"),
                            ("joint_session", "Joint Session"),
                            ("contest", "Contest"),
                        ],
                        max_length=64,
                    ),
                ),
                ("held_on", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Participation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="event.event"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name="PerformedRole",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "participation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="event.participation",
                    ),
                ),
                (
                    "role",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="event.role"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="participation",
            name="roles",
            field=models.ManyToManyField(
                through="event.PerformedRole", to="event.role"
            ),
        ),
        migrations.AddField(
            model_name="participation",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="users",
            field=models.ManyToManyField(
                related_name="events",
                through="event.Participation",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
