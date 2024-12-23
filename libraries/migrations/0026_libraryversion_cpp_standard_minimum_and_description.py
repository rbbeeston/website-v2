# Generated by Django 4.2.16 on 2024-11-08 23:03

from django.db import migrations, models
import django.db.migrations.operations.special


def populate_cpp_standard_minimum_and_description(apps, schema_editor):
    # populate cpp minimum and description from the values in the 'data' columns
    LibraryVersion = apps.get_model("libraries", "LibraryVersion")
    for library_version in LibraryVersion.objects.all():
        updated = False
        if library_version.data.get("cxxstd"):
            library_version.cpp_standard_minimum = library_version.data["cxxstd"]
            updated = True
        if library_version.data.get("description"):
            library_version.description = library_version.data["description"]
            updated = True
        if updated:
            library_version.save()


class Migration(migrations.Migration):

    replaces = [('libraries', '0026_libraryversion_cpp_standard_minimum'), ('libraries', '0027_populate_cpp_standard_minimum'), ('libraries', '0028_libraryversion_description'), ('libraries', '0029_populate_library_version_description')]

    dependencies = [
        ('libraries', '0025_libraryversion_deletions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name="libraryversion",
            name="cpp_standard_minimum",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='libraryversion',
            name='description',
            field=models.TextField(blank=True, help_text='The description of the library.', null=True),
        ),
        migrations.RunPython(populate_cpp_standard_minimum_and_description, migrations.RunPython.noop)
    ]
