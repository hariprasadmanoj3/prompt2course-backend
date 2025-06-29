import requests
import json

BASE_URL = "http://localhost:8000/api"

def test_health_check():
    """Test if API is running"""
    try:
        response = requests.get(f"{BASE_URL}/health/")
        print(f"Health Check: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"Health check failed: {e}")
        return False

def test_course_generation():
    """Test course generation"""
    try:
        data = {"topic": "Python Basics"}
        response = requests.post(f"{BASE_URL}/generate-course/", json=data)
        print(f"\nCourse Generation: {response.status_code}")
        
        if response.status_code == 201:
            result = response.json()
            print(f"Success: {result['success']}")
            print(f"Course ID: {result['course']['id']}")
            print(f"Title: {result['course']['course_title']}")
            return result['course']['id']
        else:
            print(f"Error: {response.json()}")
            return None
            
    except Exception as e:
        print(f"Course generation failed: {e}")
        return None

def test_course_retrieval(course_id):
    """Test getting course details"""
    try:
        response = requests.get(f"{BASE_URL}/course/{course_id}/")
        print(f"\nCourse Retrieval: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            lessons = result['course']['lessons']
            print(f"Found {len(lessons)} lessons")
            for i, lesson in enumerate(lessons, 1):
                print(f"  Lesson {i}: {lesson['title']}")
        else:
            print(f"Error: {response.json()}")
            
    except Exception as e:
        print(f"Course retrieval failed: {e}")

if __name__ == "__main__":
    print("Testing Prompt2Course API...")
    
    # Test 1: Health check
    if not test_health_check():
        print("❌ API is not running. Start Django server first!")
        exit(1)
    
    print("✅ API is healthy!")
    
    # Test 2: Generate course
    course_id = test_course_generation()
    if course_id:
        print("✅ Course generation works!")
        
        # Test 3: Retrieve course
        test_course_retrieval(course_id)
        print("✅ Course retrieval works!")
    else:
        print("❌ Course generation failed!")