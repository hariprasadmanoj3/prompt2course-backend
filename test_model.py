#!/usr/bin/env python
import os
import django
from django.conf import settings

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prompt2course.settings')
django.setup()

from courses.models import Course

def test_model():
    print("Testing Course model...")
    
    # Test creating a course
    course = Course(
        title="Test Course",
        description="Test description",
        topic="Testing",
        created_by="test_user"
    )
    
    print(f"Course created: {course}")
    print(f"Title: {course.title}")
    print(f"Description: {course.description}")
    print(f"Topic: {course.topic}")
    print(f"Created by: {course.created_by}")
    
    print("✅ Model test passed!")

if __name__ == "__main__":
    test_model()