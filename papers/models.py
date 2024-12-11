from django.db import models

from django.db import models

class ResearchPaper(models.Model):
    title = models.CharField(max_length=255)  
    conference_name = models.CharField(max_length=255, null=True, blank=True)  
    authors = models.CharField(max_length=255)  
    date = models.DateField() 
    abstract = models.TextField(null=True, blank=True) 
    paper_file = models.FileField(upload_to='research_papers/')  
    certificate = models.ImageField(upload_to='certificates/', null=True, blank=True)  

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']  # Show the most recent papers first

