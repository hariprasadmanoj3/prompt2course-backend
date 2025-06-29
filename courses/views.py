from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
from .models import Course
from .serializers import CourseSerializer
import logging

logger = logging.getLogger(__name__)

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    def create(self, request):
        """Create a new course from a topic prompt"""
        try:
            topic = request.data.get('topic', '').strip()
            created_by = request.data.get('created_by', 'anonymous')
            
            if not topic:
                return Response(
                    {'error': 'Topic is required'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Generate course title and description
            title = f"Complete Guide to {topic}"
            description = f"A comprehensive course covering all aspects of {topic}. Learn from basics to advanced concepts with practical examples and real-world applications."
            
            # Create the course
            course = Course.objects.create(
                title=title,
                description=description,
                topic=topic,
                created_by=created_by
            )
            
            logger.info(f"[{timezone.now()}] Course created: {course.title} by {created_by}")
            
            serializer = self.get_serializer(course)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            logger.error(f"Error creating course: {str(e)}")
            return Response(
                {'error': 'Failed to create course'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def list(self, request):
        """List all courses with enhanced data"""
        try:
            courses = self.get_queryset()
            serializer = self.get_serializer(courses, many=True)
            
            logger.info(f"[{timezone.now()}] Courses retrieved: {courses.count()} courses")
            
            return Response(serializer.data)
        except Exception as e:
            logger.error(f"Error listing courses: {str(e)}")
            return Response(
                {'error': 'Failed to retrieve courses'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=False, methods=['get'])
    def stats(self, request):
        """Get course statistics"""
        try:
            total_courses = Course.objects.count()
            recent_courses = Course.objects.filter(
                created_at__gte=timezone.now() - timezone.timedelta(days=7)
            ).count()
            
            stats_data = {
                'total_courses': total_courses,
                'recent_courses': recent_courses,
                'creators': Course.objects.values_list('created_by', flat=True).distinct().count(),
                'latest_course': None
            }
            
            if total_courses > 0:
                latest = Course.objects.first()
                stats_data['latest_course'] = {
                    'title': latest.title,
                    'created_at': latest.created_at,
                    'created_by': latest.created_by
                }
            
            return Response(stats_data)
        except Exception as e:
            logger.error(f"Error getting stats: {str(e)}")
            return Response({'error': 'Failed to get statistics'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)