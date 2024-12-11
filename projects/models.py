from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    github = models.URLField(max_length=500, blank=True, null=True)
    live = models.URLField(max_length=500, blank=True, null=True)
    
    # Add Taggit's TaggableManager
    tags = TaggableManager()
    
    # Timestamps 
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class  Meta:
        ordering = ['-created_at']
        verbose_name = 'project'
        verbose_name_plural = 'projects'