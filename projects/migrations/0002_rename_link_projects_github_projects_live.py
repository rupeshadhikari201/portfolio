# Generated by Django 5.1.3 on 2024-12-04 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="projects", old_name="link", new_name="github",
        ),
        migrations.AddField(
            model_name="projects",
            name="live",
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
