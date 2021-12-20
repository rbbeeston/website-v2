# Generated by Django 3.2.2 on 2021-12-16 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('versions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VersionFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checksum', models.CharField(default=None, max_length=64, unique=True)),
                ('file', models.FileField(upload_to='uploads/')),
                ('operating_system', models.CharField(choices=[('Unix', 'Unix'), ('Windows', 'Windows')], max_length=15)),
            ],
        ),
        migrations.RemoveField(
            model_name='version',
            name='checksum',
        ),
        migrations.RemoveField(
            model_name='version',
            name='file',
        ),
        migrations.AddField(
            model_name='version',
            name='files',
            field=models.ManyToManyField(to='versions.VersionFile'),
        ),
    ]
