#!/usr/bin/env python
import os
import sys
import django

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prompt2course_backend.settings')
django.setup()

from courses.models import Course
from datetime import datetime

def test_database():
    print(f"[{datetime.now()}] Testing database for hariprasadmanoj3...")
    
    try:
        # Test database connection
        courses_count = Course.objects.count()
        print(f"✅ Database connected successfully")
        print(f"📊 Total courses in database: {courses_count}")
        
        # List all courses
        if courses_count > 0:
            print("\n📚 Existing courses:")
            for i, course in enumerate(Course.objects.all(), 1):
                print(f"  {i}. {course.topic} (ID: {course.id}) - Status: {course.status}")
        else:
            print("📝 No courses found in database")
            
        # Test creating a sample course
        print(f"\n🧪 Testing course creation...")
        test_course = Course.objects.create(
            topic="Test Course for hariprasadmanoj3",
            course_data={
                "course_title": "Test Course",
                "total_lessons": 1,
                "lessons": [{
                    "title": "Test Lesson",
                    "content": "This is a test lesson for hariprasadmanoj3"
                }]
            },
            status='completed',
            created_by='hariprasadmanoj3'
        )
        print(f"✅ Test course created successfully with ID: {test_course.id}")
        
        # Clean up test course
        test_course.delete()
        print(f"🧹 Test course cleaned up")
        
        print(f"\n🎉 All tests passed! Backend is working correctly for hariprasadmanoj3")
        
    except Exception as e:
        print(f"❌ Error testing database: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_database()