# Generated by Django 4.2 on 2023-05-12 18:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Entry",
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
                ("slug", models.SlugField()),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, default="")),
                ("external_url", models.URLField(blank=True, default="")),
                ("image", models.ImageField(blank=True, null=True, upload_to="news")),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("publish_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Entries",
            },
        ),
        migrations.CreateModel(
            name="BlogPost",
            fields=[
                (
                    "entry_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="news.entry",
                    ),
                ),
                ("body", models.TextField()),
                ("abstract", models.CharField(max_length=256)),
            ],
            bases=("news.entry",),
        ),
        migrations.CreateModel(
            name="Link",
            fields=[
                (
                    "entry_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="news.entry",
                    ),
                ),
            ],
            bases=("news.entry",),
        ),
        migrations.CreateModel(
            name="Poll",
            fields=[
                (
                    "entry_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="news.entry",
                    ),
                ),
            ],
            bases=("news.entry",),
        ),
        migrations.CreateModel(
            name="Video",
            fields=[
                (
                    "entry_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="news.entry",
                    ),
                ),
            ],
            bases=("news.entry",),
        ),
        migrations.CreateModel(
            name="PollChoice",
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
                ("wording", models.CharField(max_length=200)),
                ("order", models.PositiveIntegerField()),
                ("votes", models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                (
                    "poll",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="news.poll"
                    ),
                ),
            ],
        ),
    ]
