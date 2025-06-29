from django.db import models
from django.utils import timezone

class Course(models.Model):
    title = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    created_by = models.CharField(max_length=100, default='user')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Auto-generate title and description if not provided
        if not self.title and self.topic:
            self.title = f"Complete Guide to {self.topic}"
        
        if not self.description and self.topic:
            self.description = f"A comprehensive course covering all aspects of {self.topic}"
        
        if not self.content and self.topic:
            self.content = f"""# {self.title}

## Introduction
Welcome to this comprehensive course on {self.topic}.

## What You'll Learn
- Fundamentals of {self.topic}
- Practical applications
- Best practices
- Real-world examples

## Course Structure
This course is designed to take you from beginner to advanced level in {self.topic}.

## Getting Started
Let's begin your learning journey!"""
        
        super().save(*args, **kwargs)