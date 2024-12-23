# Generated by Django 5.1.3 on 2024-12-11 11:22

import taggit.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        (
            "taggit",
            "0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Books",
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
                (
                    "title",
                    models.CharField(help_text="Title of the book", max_length=255),
                ),
                (
                    "author",
                    models.CharField(help_text="Author of the book", max_length=255),
                ),
                (
                    "genre",
                    models.CharField(
                        help_text="Genre of the book (e.g., Fiction, Non-fiction)",
                        max_length=100,
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Short description or synopsis of the book",
                        null=True,
                    ),
                ),
                (
                    "publication_date",
                    models.DateField(help_text="Date when the book was published"),
                ),
                (
                    "is_favorite",
                    models.BooleanField(default=False, help_text="Mark as favorite"),
                ),
                (
                    "cover_image",
                    models.ImageField(
                        blank=True,
                        help_text="Upload a cover image for the book",
                        null=True,
                        upload_to="book_covers/",
                    ),
                ),
                (
                    "author_image",
                    models.ImageField(
                        blank=True,
                        help_text="Upload a cover image for the book",
                        null=True,
                        upload_to="book_authors/",
                    ),
                ),
                (
                    "tags",
                    taggit.managers.TaggableManager(
                        help_text="Add tags for categorizing books (e.g., Fantasy, Bestseller)",
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="Tags",
                    ),
                ),
            ],
            options={"ordering": ["-publication_date"],},
        ),
    ]
