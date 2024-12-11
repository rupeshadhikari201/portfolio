from django.contrib import admin
from .models import ResearchPaper

@admin.register(ResearchPaper)
class ResearchPaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'conference_name', 'date', 'authors')
    search_fields = ('title', 'conference_name', 'authors')
