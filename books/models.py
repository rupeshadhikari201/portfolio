from django.db import models
from taggit.managers import TaggableManager

class Books(models.Model):
    title = models.CharField(max_length=255, help_text="Title of the book")
    author = models.CharField(max_length=255, help_text="Author of the book")
    genre = models.CharField(max_length=100, help_text="Genre of the book (e.g., Fiction, Non-fiction)")
    description = models.TextField(blank=True, null=True, help_text="Short description or synopsis of the book")
    publication_date = models.DateField(help_text="Date when the book was published")
    is_favorite = models.BooleanField(default=False, help_text="Mark as favorite")
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True, help_text="Upload a cover image for the book")
    author_image = models.ImageField(upload_to='book_authors/', blank=True, null=True, help_text="Upload a cover image for the book")

    # Tags for categorization
    tags = TaggableManager(help_text="Add tags for categorizing books (e.g., Fantasy, Bestseller)")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publication_date']  # Order books by newest publication date first
