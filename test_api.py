#!/usr/bin/env python
import os
import django
from django.conf import settings

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prompt2course.settings')
django.setup()

from courses.models import Course
from datetime import datetime

def test_api():
    print(f"[{datetime.now()}] Testing Django API...")
    
    # Test database connection
    try:
        course_count = Course.objects.count()
        print(f"✅ Database connected. Found {course_count} courses.")
        
        # List all courses
        courses = Course.objects.all()
        for course in courses:
            print(f"  - {course.title} (by {course.created_by})")
            
    except Exception as e:
        print(f"❌ Database error: {e}")
    
    print("✅ API test complete!")

if __name__ == "__main__":
    test_api()