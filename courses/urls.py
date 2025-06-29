from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet

# Create router and register viewsets
router = DefaultRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]