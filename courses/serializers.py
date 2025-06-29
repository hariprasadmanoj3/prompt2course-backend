from rest_framework import serializers
from .models import Course, CourseGenerationLog

class CourseSerializer(serializers.ModelSerializer):
    """Basic course serializer for list views"""
    
    total_lessons = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    
    class Meta:
        model = Course
        fields = [
            'id', 'topic', 'created_at', 'updated_at', 
            'total_lessons', 'status'
        ]
    
    def get_total_lessons(self, obj):
        return obj.get_total_lessons()
    
    def get_status(self, obj):
        content = obj.content or {}
        return content.get('status', 'unknown')

class CourseDetailSerializer(serializers.ModelSerializer):
    """Detailed course serializer with full content"""
    
    course_title = serializers.SerializerMethodField()
    course_description = serializers.SerializerMethodField()
    difficulty_level = serializers.SerializerMethodField()
    estimated_duration = serializers.SerializerMethodField()
    lessons = serializers.SerializerMethodField()
    generation_logs = serializers.SerializerMethodField()
    
    class Meta:
        model = Course
        fields = [
            'id', 'topic', 'created_at', 'updated_at',
            'course_title', 'course_description', 'difficulty_level',
            'estimated_duration', 'lessons', 'generation_logs'
        ]
    
    def get_course_title(self, obj):
        return obj.content.get('course_title', f"Learn {obj.topic}")
    
    def get_course_description(self, obj):
        return obj.content.get('course_description', '')
    
    def get_difficulty_level(self, obj):
        return obj.content.get('difficulty_level', 'beginner')
    
    def get_estimated_duration(self, obj):
        return obj.content.get('estimated_duration', 'Unknown')
    
    def get_lessons(self, obj):
        return obj.content.get('lessons', [])
    
    def get_generation_logs(self, obj):
        # Only include logs in debug mode
        logs = obj.logs.all().order_by('-created_at')[:5]
        return [{
            'step': log.step,
            'status': log.status,
            'created_at': log.created_at,
            'execution_time': log.execution_time
        } for log in logs]

class CourseGenerationLogSerializer(serializers.ModelSerializer):
    """Serializer for course generation logs"""
    
    class Meta:
        model = CourseGenerationLog
        fields = ['step', 'status', 'error_message', 'execution_time', 'created_at']