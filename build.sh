#!/usr/bin/env bash
# exit on error
set -o errexit

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Starting build process..."

# Install dependencies
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Installing dependencies..."
pip install -r requirements.txt

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Collecting static files..."
python manage.py collectstatic --no-input

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Creating fresh migrations..."
python manage.py makemigrations

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Running migrations..."
python manage.py migrate

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Creating superuser..."
python manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('Superuser created: admin/admin123')
else:
    print('Superuser already exists')
"

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Creating sample data..."
python manage.py shell -c "
from courses.models import Course
from datetime import datetime

# Clear existing courses
Course.objects.all().delete()

# Create sample courses
sample_courses = [
    {
        'title': 'JavaScript Fundamentals',
        'description': 'Learn the basics of JavaScript programming including variables, functions, objects, and DOM manipulation. Perfect for beginners starting their web development journey.',
        'topic': 'JavaScript Fundamentals',
        'created_by': 'hariprasadmanoj3'
    },
    {
        'title': 'Python for Data Science',
        'description': 'Master Python programming for data analysis, including pandas, numpy, matplotlib, and basic machine learning concepts.',
        'topic': 'Python for Data Science',
        'created_by': 'hariprasadmanoj3'
    },
    {
        'title': 'React.js Complete Guide',
        'description': 'Build modern web applications with React.js. Learn components, state management, hooks, and deployment strategies.',
        'topic': 'React.js Complete Guide',
        'created_by': 'hariprasadmanoj3'
    },
    {
        'title': 'Machine Learning Basics',
        'description': 'Introduction to machine learning concepts, algorithms, and practical implementation using Python and scikit-learn.',
        'topic': 'Machine Learning Basics',
        'created_by': 'hariprasadmanoj3'
    },
    {
        'title': 'Digital Photography Masterclass',
        'description': 'Learn the art of digital photography including composition, lighting, camera settings, and post-processing techniques.',
        'topic': 'Digital Photography',
        'created_by': 'hariprasadmanoj3'
    },
    {
        'title': 'Web Design with CSS',
        'description': 'Create beautiful, responsive websites using modern CSS techniques, flexbox, grid, and animations.',
        'topic': 'Web Design',
        'created_by': 'hariprasadmanoj3'
    }
]

created_count = 0
for course_data in sample_courses:
    course = Course.objects.create(**course_data)
    created_count += 1
    print(f'Created course: {course.title}')

print(f'Successfully created {created_count} sample courses')
"

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Build complete! ✅"
echo "Backend is ready at: https://prompt2course-backend-1.onrender.com"
echo "API endpoint: https://prompt2course-backend-1.onrender.com/api/courses/"