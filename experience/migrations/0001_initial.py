# Generated by Django 5.1.3 on 2024-12-04 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Experience",
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
                ("job_title", models.CharField(max_length=200)),
                ("company_name", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(blank=True, null=True)),
                ("link", models.URLField(blank=True, null=True)),
                (
                    "certificate",
                    models.FileField(blank=True, null=True, upload_to="certificates/"),
                ),
            ],
            options={"ordering": ["-start_date"],},
        ),
    ]
