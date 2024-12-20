# Generated by Django 4.2.16 on 2024-11-12 17:15

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.functions.comparison
import django.db.models.lookups


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Channel",
            fields=[
                (
                    "id",
                    models.CharField(max_length=16, primary_key=True, serialize=False),
                ),
                ("name", models.TextField()),
                ("topic", models.TextField()),
                ("purpose", models.TextField()),
                ("last_update_ts", models.CharField(max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="SlackUser",
            fields=[
                (
                    "id",
                    models.CharField(max_length=16, primary_key=True, serialize=False),
                ),
                ("name", models.TextField()),
                ("real_name", models.TextField()),
                ("email", models.TextField()),
                ("image_48", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="Thread",
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
                ("thread_ts", models.CharField(max_length=32)),
                ("last_update_ts", models.CharField(max_length=32, null=True)),
                ("db_created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "channel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="slack.channel"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SlackActivityBucket",
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
                ("day", models.DateField()),
                ("count", models.PositiveIntegerField()),
                (
                    "channel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="slack.channel"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="slack.slackuser",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SeenMessage",
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
                ("ts", models.CharField(max_length=32)),
                ("db_created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "channel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="slack.channel"
                    ),
                ),
                (
                    "thread",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="slack.thread",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ChannelUpdateGap",
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
                ("oldest_message_ts", models.CharField(max_length=32, null=True)),
                ("newest_message_ts", models.CharField(max_length=32, null=True)),
                (
                    "channel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="slack.channel"
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="thread",
            constraint=models.CheckConstraint(
                check=django.db.models.lookups.GreaterThanOrEqual(
                    django.db.models.functions.comparison.Cast(
                        "last_update_ts", output_field=models.FloatField()
                    ),
                    django.db.models.functions.comparison.Cast(
                        "thread_ts", output_field=models.FloatField()
                    ),
                ),
                name="update_newer_than_created",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="thread",
            unique_together={("channel", "thread_ts")},
        ),
        migrations.AlterUniqueTogether(
            name="slackactivitybucket",
            unique_together={("channel", "day", "user")},
        ),
        migrations.AlterUniqueTogether(
            name="seenmessage",
            unique_together={("channel", "ts")},
        ),
        migrations.AddConstraint(
            model_name="channelupdategap",
            constraint=models.CheckConstraint(
                check=django.db.models.lookups.GreaterThan(
                    django.db.models.functions.comparison.Cast(
                        "newest_message_ts", output_field=models.FloatField()
                    ),
                    django.db.models.functions.comparison.Cast(
                        "oldest_message_ts", output_field=models.FloatField()
                    ),
                ),
                name="newest_newer_than_oldest",
            ),
        ),
    ]
