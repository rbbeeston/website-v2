# Generated by Django 3.2.2 on 2023-03-03 21:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("libraries", "0004_auto_20230130_1830"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="library",
            name="maintainers",
        ),
        migrations.AddField(
            model_name="libraryversion",
            name="maintainers",
            field=models.ManyToManyField(
                related_name="maintainers", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
