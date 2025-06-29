from django.urls import path
from .views import (
    GenerateCourseView, 
    CourseDetailView, 
    CourseListView, 
    CourseSearchView,
    HealthCheckView
)

app_name = 'courses'

urlpatterns = [
    # Course generation
    path('generate-course/', GenerateCourseView.as_view(), name='generate-course'),
    
    # Course retrieval
    path('course/<uuid:course_id>/', CourseDetailView.as_view(), name='course-detail'),
    path('courses/', CourseListView.as_view(), name='course-list'),
    
    # Search
    path('search-courses/', CourseSearchView.as_view(), name='course-search'),
    
    # Health check
    path('health/', HealthCheckView.as_view(), name='health-check'),
]