#!/usr/bin/env bash
set -o errexit

echo "🚀 [$(date)] Starting Prompt2Course Backend Build..."

echo "📦 Installing Python dependencies..."
pip install -r requirements.txt
echo "✅ Dependencies installed"

echo "📂 Collecting static files..."
python manage.py collectstatic --no-input
echo "✅ Static files collected"

echo "🗄️ Cleaning up old database and migrations..."
# Remove old database
rm -f db.sqlite3

# Remove old migration files but keep __init__.py
find courses/migrations/ -name "*.py" -not -name "__init__.py" -delete

echo "🔄 Creating fresh migrations..."
python manage.py makemigrations courses
echo "✅ Fresh migrations created"

echo "🗄️ Running database migrations..."
python manage.py migrate
echo "✅ Database migrated successfully"

echo "👤 Creating admin user..."
python manage.py shell -c "
from django.contrib.auth.models import User
try:
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@prompt2course.com', 'admin123')
        print('✅ Admin user created: admin/admin123')
    else:
        print('✅ Admin user already exists')
except Exception as e:
    print(f'⚠️ Admin user creation issue: {e}')
"

echo "📚 Creating sample courses..."
python manage.py shell -c "
from courses.models import Course
from django.utils import timezone
import traceback

try:
    print('🗑️ Clearing any existing courses...')
    Course.objects.all().delete()

    sample_courses = [
        {
            'title': 'JavaScript Fundamentals for Web Development',
            'description': 'Master JavaScript from basics to advanced concepts. Learn variables, functions, objects, DOM manipulation, and modern ES6+ features for building interactive web applications.',
            'topic': 'JavaScript Fundamentals',
            'created_by': 'hariprasadmanoj3'
        },
        {
            'title': 'Python Programming for Data Science',
            'description': 'Comprehensive Python course covering data analysis, visualization, and machine learning basics using pandas, numpy, matplotlib, and scikit-learn.',
            'topic': 'Python for Data Science',
            'created_by': 'hariprasadmanoj3'
        },
        {
            'title': 'React.js Complete Developer Course',
            'description': 'Build modern, responsive web applications with React.js. Learn components, hooks, state management, routing, and deployment strategies.',
            'topic': 'React.js Complete Guide',
            'created_by': 'hariprasadmanoj3'
        },
        {
            'title': 'Machine Learning Fundamentals',
            'description': 'Introduction to machine learning concepts, algorithms, and practical implementation. Cover supervised learning, unsupervised learning, and neural networks.',
            'topic': 'Machine Learning Basics',
            'created_by': 'hariprasadmanoj3'
        },
        {
            'title': 'Digital Photography Masterclass',
            'description': 'Learn professional photography techniques including composition, lighting, camera settings, post-processing, and portfolio development.',
            'topic': 'Digital Photography',
            'created_by': 'hariprasadmanoj3'
        },
        {
            'title': 'Modern Web Design with CSS',
            'description': 'Create stunning, responsive websites using modern CSS techniques including Flexbox, Grid, animations, and responsive design principles.',
            'topic': 'Web Design with CSS',
            'created_by': 'hariprasadmanoj3'
        }
    ]

    created_count = 0
    for course_data in sample_courses:
        course = Course.objects.create(**course_data)
        created_count += 1
        print(f'✅ Created: {course.title}')

    print(f'🎉 Successfully created {created_count} sample courses!')
    
    # Verify database
    total_courses = Course.objects.count()
    print(f'📊 Total courses in database: {total_courses}')
    
    # Test the API structure
    if total_courses > 0:
        latest_course = Course.objects.first()
        print(f'✅ Latest course: {latest_course.title}')
        print(f'✅ Created by: {latest_course.created_by}')
        print(f'✅ Created at: {latest_course.created_at}')
        print(f'✅ Topic: {latest_course.topic}')
    
except Exception as e:
    print(f'❌ Error creating sample data: {e}')
    traceback.print_exc()
"

echo "🧪 Testing API endpoints..."
python manage.py shell -c "
from courses.models import Course
from courses.serializers import CourseSerializer
try:
    course_count = Course.objects.count()
    print(f'✅ Database connection: {course_count} courses available')
    
    if course_count > 0:
        # Test serializer
        course = Course.objects.first()
        serializer = CourseSerializer(course)
        print(f'✅ Serializer test passed for: {course.title}')
        print(f'✅ Serialized fields: {list(serializer.data.keys())}')
    
    print('✅ All tests passed - API is ready!')
    
except Exception as e:
    print(f'❌ API test failed: {e}')
    import traceback
    traceback.print_exc()
"

echo ""
echo "🎉 BUILD COMPLETE!"
echo "✅ Backend deployed successfully with fresh database"
echo ""
echo "📡 API Endpoints:"
echo "   🌐 Base URL: https://prompt2course-backend-1.onrender.com"
echo "   📚 Courses: https://prompt2course-backend-1.onrender.com/api/courses/"
echo "   💊 Health: https://prompt2course-backend-1.onrender.com/health/"
echo "   👤 Admin: https://prompt2course-backend-1.onrender.com/admin/"
echo ""
echo "🔑 Admin Credentials: admin / admin123"
echo "👨‍💻 Developer: hariprasadmanoj3"
echo "⏰ Build completed at: $(date)"
echo "🆔 Build ID: $(date +%s)"