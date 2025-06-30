from django.db import models
from django.utils import timezone

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    topic = models.CharField(max_length=200)
    content = models.TextField(blank=True, default='')
    created_by = models.CharField(max_length=100, default='hariprasadmanoj3')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title