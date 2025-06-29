import time
from typing import Dict, Any
from ..models import Course, CourseGenerationLog
from .openai_service import OpenAIService
from .youtube_service import YouTubeService

class CourseGenerator:
    def __init__(self):
        self.openai_service = OpenAIService()
        self.youtube_service = YouTubeService()

    def generate_complete_course(self, topic: str) -> Course:
        """Main method: Generates full course for a given topic"""

        # Create initial course object (status: generating)
        course = Course.objects.create(
            topic=topic,
            content={'status': 'generating'}
        )

        try:
            # Step 1: Generate structured course content using OpenAI
            self._log_step(course, 'openai_generation', 'started')
            course_data = self.openai_service.generate_course_structure(topic)
            self._log_step(course, 'openai_generation', 'completed')

            # Step 2: Fetch YouTube video links for each lesson
            self._log_step(course, 'youtube_search', 'started')
            self._add_youtube_videos(course_data)
            self._log_step(course, 'youtube_search', 'completed')

            # Step 3: Save full course data to DB
            course.content = course_data
            course.save()

            return course

        except Exception as e:
            # Handle failures
            self._log_step(course, 'generation_failed', 'failed', str(e))
            course.content = {'status': 'failed', 'error': str(e)}
            course.save()
            raise e

    def _add_youtube_videos(self, course_data: Dict[str, Any]):
        """For each lesson, search for relevant YouTube videos"""
        for lesson in course_data.get('lessons', []):
            lesson['youtube_videos'] = []

            for query in lesson.get('youtube_search_queries', []):
                try:
                    video_results = self.youtube_service.search_educational_videos(query, max_results=1)
                    if video_results['videos']:
                        lesson['youtube_videos'].extend(video_results['videos'])
                except Exception as e:
                    print(f"Error fetching YouTube videos for query '{query}': {e}")

            # Limit to max 2 videos per lesson
            lesson['youtube_videos'] = lesson['youtube_videos'][:2]

    def _log_step(self, course: Course, step: str, status: str, error_message: str = None):
        """Log progress of each major step for debugging and tracking"""
        CourseGenerationLog.objects.create(
            course=course,
            step=step,
            status=status,
            error_message=error_message
        )
