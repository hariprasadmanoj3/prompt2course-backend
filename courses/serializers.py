from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')
    
    def create(self, validated_data):
        # Auto-generate title and description from topic if not provided
        topic = validated_data.get('topic', '')
        
        if not validated_data.get('title') and topic:
            validated_data['title'] = f"Complete Guide to {topic}"
        
        if not validated_data.get('description') and topic:
            validated_data['description'] = f"A comprehensive course covering all aspects of {topic}"
        
        if not validated_data.get('content') and topic:
            validated_data['content'] = f"""# {validated_data['title']}

## Introduction
Welcome to this comprehensive course on {topic}.

## What You'll Learn
- Fundamentals of {topic}
- Practical applications
- Best practices
- Real-world examples

## Course Structure
This course is designed to take you from beginner to advanced level in {topic}.

## Getting Started
Let's begin your learning journey!"""
        
        return super().create(validated_data)