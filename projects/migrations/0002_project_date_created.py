# Generated by Django 4.2.9 on 2024-02-28 02:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="date_created",
            field=models.DateField(default=datetime.date(2024, 2, 28)),
        ),
    ]
