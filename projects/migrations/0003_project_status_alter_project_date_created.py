# Generated by Django 4.2.9 on 2024-02-28 03:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0002_project_date_created"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="status",
            field=models.CharField(
                choices=[("I", "Incomplete"), ("C", "Complete")],
                default="I",
                max_length=1,
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="date_created",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 2, 28, 3, 26, 36, 701900, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]