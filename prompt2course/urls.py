from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.utils import timezone
from courses.views import health_check

def api_root(request):
    return JsonResponse({
        'message': 'Prompt2Course API',
        'status': 'online',
        'timestamp': timezone.now().isoformat()
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('courses.urls')),
    path('health/', health_check),
    path('', api_root),
]