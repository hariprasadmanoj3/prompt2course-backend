from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def api_root(request):
    """API root endpoint with basic info"""
    return JsonResponse({
        'message': 'Welcome to Prompt2Course API',
        'version': '1.0.0',
        'endpoints': {
            'courses': '/api/courses/',
            'admin': '/admin/',
            'health': '/api/health/'
        },
        'status': 'online',
        'timestamp': '2025-06-29T09:09:42Z'
    })

def health_check(request):
    """Health check endpoint"""
    return JsonResponse({
        'status': 'healthy',
        'service': 'prompt2course-backend',
        'timestamp': '2025-06-29T09:09:42Z'
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('courses.urls')),
    path('api/health/', health_check, name='health_check'),
    path('', api_root, name='api_root'),
]