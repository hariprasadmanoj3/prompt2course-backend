from rest_framework import viewsets, status
from rest_framework.response import Response
from django.utils import timezone
from django.http import JsonResponse
from .models import Course
from .serializers import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    def create(self, request):
        topic = request.data.get('topic', '').strip()
        created_by = request.data.get('created_by', 'hariprasadmanoj3')
        
        if not topic:
            return Response({'error': 'Topic is required'}, status=400)
        
        course = Course.objects.create(
            title=f"Complete Guide to {topic}",
            description=f"Learn {topic} from basics to advanced concepts.",
            topic=topic,
            created_by=created_by
        )
        
        serializer = self.get_serializer(course)
        return Response(serializer.data, status=201)

def health_check(request):
    return JsonResponse({
        'status': 'healthy',
        'timestamp': timezone.now().isoformat(),
        'service': 'prompt2course-backend'
    })