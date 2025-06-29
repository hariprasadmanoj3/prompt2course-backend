from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CourseViewSet,
    CourseSearchView,
    CourseDetailView,
    CourseCreateView,
    health_check,
    course_list,
    course_create
)

router = DefaultRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('health/', health_check, name='health_check'),
    path('courses/search/', CourseSearchView.as_view(), name='course_search'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('courses/create/', CourseCreateView.as_view(), name='course_create'),
    
    # Alternative function-based views
    path('course-list/', course_list, name='course_list'),
    path('course-create/', course_create, name='course_create_func'),
]