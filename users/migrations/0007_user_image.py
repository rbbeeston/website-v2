# Generated by Django 3.2.2 on 2023-02-15 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_auto_20220209_1545"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="image",
            field=models.FileField(blank=True, null=True, upload_to="profile-images"),
        ),
    ]
