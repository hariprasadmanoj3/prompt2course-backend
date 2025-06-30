#!/usr/bin/env bash
set -o errexit

echo "🚀 [$(date)] Starting build..."

pip install -r requirements.txt
echo "✅ Dependencies installed"

python manage.py collectstatic --no-input
echo "✅ Static files collected"

python manage.py makemigrations
echo "✅ Migrations created"

python manage.py migrate
echo "✅ Database migrated"

python -c "
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prompt2course.settings')
django.setup()

from courses.models import Course
from django.contrib.auth.models import User

# Create admin user
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('✅ Admin created')

# Create sample courses
Course.objects.all().delete()
courses_data = [
    {'title': 'JavaScript Fundamentals', 'description': 'Learn JavaScript basics', 'topic': 'JavaScript'},
    {'title': 'Python for Beginners', 'description': 'Learn Python programming', 'topic': 'Python'},
    {'title': 'React.js Complete Guide', 'description': 'Build React applications', 'topic': 'React'},
    {'title': 'Machine Learning Basics', 'description': 'Introduction to ML', 'topic': 'Machine Learning'},
]

for data in courses_data:
    Course.objects.create(**data)

print(f'✅ Created {len(courses_data)} courses')
"

echo "🎉 Build complete!"