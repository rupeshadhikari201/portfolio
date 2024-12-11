from django.db import models

# Create your models here.
class Experience(models.Model):
    job_title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    certificate = models.FileField(upload_to='certificates/', null=True, blank=True)
    company_logo = models.ImageField(upload_to='logo/', null=True, blank=True)
    
    def __str__(self):
        return self.job_title
    
    class Meta:
        ordering = ['-start_date']
    