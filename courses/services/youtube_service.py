from django.conf import settings
from typing import List, Dict, Any
import time

# Try importing googleapiclient only if available
try:
    from googleapiclient.discovery import build
except ImportError:
    build = None  # Handle missing package in mock mode

class YouTubeService:
    def __init__(self):
        if build and settings.YOUTUBE_API_KEY:
            self.youtube = build('youtube', 'v3', developerKey=settings.YOUTUBE_API_KEY)
        else:
            self.youtube = None  # Fallback mock mode if no API key

    def search_educational_videos(self, query: str, max_results: int = 2) -> Dict[str, Any]:
        if not self.youtube:
            # ✅ Mock response for testing without YouTube API
            return {
                'videos': [
                    {
                        'title': f"Sample Video for {query}",
                        'description': f"Dummy video description for {query}.",
                        'video_id': 'dummy123',
                        'url': f"https://www.youtube.com/watch?v=dummy123",
                        'embed_url': f"https://www.youtube.com/embed/dummy123",
                        'thumbnail': 'https://via.placeholder.com/120x90.png?text=Thumbnail',
                        'channel_title': 'Mock Channel',
                        'published_at': '2025-06-28T00:00:00Z'
                    }
                ],
                'search_metadata': {
                    'query': query,
                    'execution_time': 0.1,
                    'results_found': 1
                }
            }

        try:
            start_time = time.time()
            search_response = self.youtube.search().list(
                q=f"{query} tutorial explanation",
                part='snippet',
                type='video',
                maxResults=max_results,
                order='relevance',
                videoDuration='medium',
                videoDefinition='high'
            ).execute()

            videos = []
            for item in search_response['items']:
                videos.append({
                    'title': item['snippet']['title'],
                    'description': item['snippet']['description'],
                    'video_id': item['id']['videoId'],
                    'url': f"https://www.youtube.com/watch?v={item['id']['videoId']}",
                    'embed_url': f"https://www.youtube.com/embed/{item['id']['videoId']}",
                    'thumbnail': item['snippet']['thumbnails']['medium']['url'],
                    'channel_title': item['snippet']['channelTitle'],
                    'published_at': item['snippet']['publishedAt']
                })

            execution_time = time.time() - start_time

            return {
                'videos': videos,
                'search_metadata': {
                    'query': query,
                    'execution_time': execution_time,
                    'results_found': len(videos)
                }
            }

        except Exception as e:
            raise Exception(f"YouTube API error: {str(e)}")
