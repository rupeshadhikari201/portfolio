from django.contrib import admin
from .models import Books

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'publication_date', 'is_favorite')
    list_filter = ('genre', 'is_favorite', 'tags')
    search_fields = ('title', 'author', 'tags__name')
