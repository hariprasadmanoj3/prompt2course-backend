from django.core.management.base import BaseCommand
from courses.models import Course
from datetime import datetime

class Command(BaseCommand):
    help = 'Create sample course data'

    def handle(self, *args, **options):
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
                'title': 'Digital Photography',
                'description': 'Learn the art of digital photography including composition, lighting, camera settings, and post-processing techniques.',
                'topic': 'Digital Photography',
                'created_by': 'hariprasadmanoj3'
            }
        ]
        
        for course_data in sample_courses:
            course = Course.objects.create(**course_data)
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created course "{course.title}"')
            )
        
        self.stdout.write(
            self.style.SUCCESS(f'Created {len(sample_courses)} sample courses')
        )