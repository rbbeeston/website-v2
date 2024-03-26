# Generated by Django 4.2.2 on 2024-01-30 17:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("libraries", "0017_merge_20230919_2029"),
    ]

    operations = [
        migrations.AddField(
            model_name="libraryversion",
            name="missing_docs",
            field=models.BooleanField(
                default=False,
                help_text="If true, then there are not docs for this version of this library.",
            ),
        ),
    ]