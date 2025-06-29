from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id', 
            'title', 
            'description', 
            'topic', 
            'content',
            'created_by', 
            'created_at', 
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def to_representation(self, instance):
        """Add computed fields to the serialized data"""
        data = super().to_representation(instance)
        
        # Add helpful computed fields
        data['time_ago'] = self.get_time_ago(instance.created_at)
        data['word_count'] = len(instance.content.split()) if instance.content else 0
        data['estimated_reading_time'] = max(1, (len(instance.content.split()) // 200)) if instance.content else 1
        
        return data
    
    def get_time_ago(self, created_at):
        """Calculate time ago string"""
        from django.utils import timezone
        
        now = timezone.now()
        diff = now - created_at
        
        if diff.days > 0:
            return f"{diff.days} day{'s' if diff.days != 1 else ''} ago"
        elif diff.seconds > 3600:
            hours = diff.seconds // 3600
            return f"{hours} hour{'s' if hours != 1 else ''} ago"
        elif diff.seconds > 60:
            minutes = diff.seconds // 60
            return f"{minutes} minute{'s' if minutes != 1 else ''} ago"
        else:
            return "Just now"