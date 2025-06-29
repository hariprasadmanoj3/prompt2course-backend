from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from courses.views import GenerateCourseView, CourseDetailView, CourseListView, SearchCoursesView
import json

@csrf_exempt
def api_health(request):
    """Health check endpoint"""
    return JsonResponse({
        'status': 'healthy',
        'message': 'Prompt2Course API is running successfully',
        'timestamp': '2025-06-28 20:52:03',
        'user': 'hariprasadmanoj3',
        'django_version': '4.2.x',
        'debug': True
    })

@csrf_exempt
def api_debug(request):
    """Debug endpoint to check what's happening"""
    from courses.models import Course
    
    try:
        courses_count = Course.objects.count()
        all_courses = list(Course.objects.values('id', 'topic', 'status', 'created_at'))
        
        return JsonResponse({
            'success': True,
            'debug_info': {
                'total_courses': courses_count,
                'courses': all_courses,
                'timestamp': '2025-06-28 20:52:03',
                'user': 'hariprasadmanoj3'
            }
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e),
            'timestamp': '2025-06-28 20:52:03'
        })

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Debug endpoints
    path('api/health/', api_health, name='api_health'),
    path('api/debug/', api_debug, name='api_debug'),
    
    # Course API endpoints
    path('api/generate-course/', GenerateCourseView.as_view(), name='generate_course'),
    path('api/course/<uuid:course_id>/', CourseDetailView.as_view(), name='course_detail'),
    path('api/courses/', CourseListView.as_view(), name='course_list'),
    path('api/search-courses/', SearchCoursesView.as_view(), name='search_courses'),
]