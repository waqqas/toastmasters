# Generated by Django 4.1 on 2022-09-04 03:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_user_last_awards_calculation"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("gamification", "0004_award_data"),
    ]

    operations = [
        migrations.CreateModel(
            name="AwardedAward",
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
            ],
        ),
        migrations.AddField(
            model_name="award",
            name="user",
            field=models.ManyToManyField(
                related_name="awards",
                through="gamification.AwardedAward",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="awardedaward",
            name="award",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="gamification.award"
            ),
        ),
        migrations.AddField(
            model_name="awardedaward",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
