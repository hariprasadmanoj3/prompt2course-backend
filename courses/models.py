import uuid
from django.db import models
from django.utils import timezone

class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    topic = models.CharField(max_length=200, help_text="The topic of the course")
    course_data = models.JSONField(default=dict, help_text="Complete course content including lessons and quizzes")
    status = models.CharField(
        max_length=20, 
        choices=[
            ('generating', 'Generating'),
            ('completed', 'Completed'),
            ('failed', 'Failed'),
        ],
        default='generating',
        help_text="Current status of the course generation"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100, default='hariprasadmanoj3', help_text="User who created the course")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return f"Course: {self.topic} (ID: {str(self.id)[:8]}...)"
    
    @property
    def total_lessons(self):
        """Get the total number of lessons in this course"""
        return self.course_data.get('total_lessons', 0) if self.course_data else 0
    
    @property
    def lesson_count(self):
        """Get the actual count of lessons in the course data"""
        lessons = self.course_data.get('lessons', []) if self.course_data else []
        return len(lessons)
    
    def save(self, *args, **kwargs):
        # Update the timestamp whenever saved
        if not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)