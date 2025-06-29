import json
import uuid
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.views import View
from .models import Course
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

@method_decorator(csrf_exempt, name='dispatch')
class GenerateCourseView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            topic = data.get('topic', '').strip()
            
            if not topic:
                return JsonResponse({
                    'success': False,
                    'error': 'Topic is required'
                }, status=400)

            print(f"[2025-06-28 20:47:46] User hariprasadmanoj3 generating course for topic: {topic}")
            
            # Generate comprehensive course content
            course_data = self.generate_course_content(topic)
            
            # Create course in database
            course = Course.objects.create(
                topic=topic,
                course_data=course_data,
                status='completed',
                created_by='hariprasadmanoj3'
            )
            
            # Verify the course was saved
            saved_course = Course.objects.get(id=course.id)
            print(f"[2025-06-28 20:47:46] Course saved successfully with ID: {saved_course.id}")
            print(f"[2025-06-28 20:47:46] Total courses in database: {Course.objects.count()}")
            
            response_data = {
                'success': True,
                'message': 'Course generated successfully!',
                'course': {
                    'id': str(course.id),
                    'topic': course.topic,
                    'status': course.status,
                    'created_at': course.created_at.isoformat(),
                    'created_by': course.created_by,
                    'total_lessons': course_data.get('total_lessons', 0),
                    **course_data
                }
            }
            
            print(f"[2025-06-28 20:47:46] Returning course data with ID: {response_data['course']['id']}")
            return JsonResponse(response_data, status=201)
            
        except json.JSONDecodeError:
            print(f"[2025-06-28 20:47:46] JSON decode error for hariprasadmanoj3")
            return JsonResponse({
                'success': False,
                'error': 'Invalid JSON data'
            }, status=400)
        except Exception as e:
            print(f"[2025-06-28 20:47:46] Error generating course for hariprasadmanoj3: {str(e)}")
            import traceback
            traceback.print_exc()
            return JsonResponse({
                'success': False,
                'error': 'Failed to generate course'
            }, status=500)

    def generate_course_content(self, topic):
        """Generate comprehensive course content with lessons and quizzes for hariprasadmanoj3"""
        
        print(f"[2025-06-28 20:47:46] Generating detailed content for hariprasadmanoj3: {topic}")
        
        # Enhanced course content generation
        course_content = {
            "course_title": f"Complete Guide to {topic}",
            "course_description": f"Master {topic} with this comprehensive course covering everything from basics to advanced concepts. Built with AI specifically for hariprasadmanoj3 to provide structured, progressive learning.",
            "difficulty_level": "Beginner",
            "estimated_duration": "3-4 hours",
            "total_lessons": 5,
            "created_by": "hariprasadmanoj3",
            "created_at": "2025-06-28 20:47:46",
            "lessons": []
        }
        
        # Generate 5 comprehensive lessons (using the same content as before but abbreviated for brevity)
        lessons_templates = [
            {
                "title": f"Introduction to {topic}",
                "content": f"""Welcome to your comprehensive journey learning {topic}, hariprasadmanoj3!

🎯 **What You'll Learn in This Lesson:**
In this foundational lesson, we'll establish a solid understanding of {topic} and prepare you for the exciting journey ahead.

📚 **Core Topics Covered:**

• **What is {topic}?**
  {topic} is a fundamental concept that plays a crucial role in modern technology and problem-solving. Understanding its principles will open doors to countless opportunities in your learning and career journey.

• **Why {topic} Matters in 2025**
  In today's rapidly evolving digital landscape, {topic} skills are more valuable than ever. Companies across all industries are seeking professionals who understand {topic}.

• **Real-World Applications**
  From everyday applications to cutting-edge innovations, {topic} is everywhere around us. Major tech companies like Google, Microsoft, and Meta use {topic} to power their most innovative products.

💡 **Key Takeaways:**
By the end of this lesson, you'll have a clear understanding of what {topic} is, why it's important, and how it fits into the broader technology ecosystem.

🚀 **What's Next:**
In our next lesson, we'll dive into the core concepts that make {topic} work, with practical examples you can follow along with.

Remember, hariprasadmanoj3: Every expert was once a beginner. Your {topic} journey starts here! 🌟""",
                "learning_objectives": [
                    f"Understand the fundamental definition and scope of {topic}",
                    f"Identify key applications and real-world use cases of {topic}",
                    f"Learn essential {topic} terminology and foundational concepts",
                    "Establish a clear, personalized learning roadmap",
                    "Build confidence and motivation for advanced topics ahead"
                ],
                "key_concepts": [
                    "Fundamentals",
                    "Core Principles", 
                    "Basic Terminology",
                    "Real-world Applications",
                    "Learning Strategy"
                ]
            },
            {
                "title": f"Core Concepts and Principles of {topic}",
                "content": f"""Great progress, hariprasadmanoj3! Now let's dive deep into the core concepts that make {topic} powerful and versatile.

🧠 **Mastering the Foundation:**

• **Understanding Core Principles**
  Every powerful technology is built on solid principles. In {topic}, these principles form the backbone of everything you'll learn.

• **The {topic} Methodology Framework**
  Professional practitioners follow a proven methodology when working with {topic}. This systematic approach will become your go-to framework.

🔧 **Hands-On Learning Experience:**
You'll work through carefully designed exercises that build your skills progressively and demonstrate real-world applications.

Ready to put these concepts into action? Our next lesson focuses on practical applications and real-world projects! 🎯""",
                "learning_objectives": [
                    f"Master the fundamental principles that govern {topic}",
                    "Apply core concepts confidently to practical scenarios", 
                    "Recognize and implement common patterns and methodologies",
                    "Develop systematic problem-solving approaches",
                    "Build practical skills through hands-on exercises"
                ],
                "key_concepts": [
                    "Core Principles",
                    "Systematic Methodology",
                    "Professional Best Practices",
                    "Hands-on Implementation",
                    "Problem-Solving Framework"
                ]
            },
            {
                "title": f"Practical Applications and Real-World Projects",
                "content": f"""Outstanding progress, hariprasadmanoj3! Now it's time to transform your theoretical knowledge into practical, real-world skills.

🚀 **From Theory to Real-World Impact:**
This is where your {topic} journey becomes truly exciting! You'll discover how the concepts you've mastered translate into solutions that solve real problems.

🛠️ **Comprehensive Project Portfolio:**
Build complete projects that demonstrate your growing expertise and create impressive portfolio pieces.

🔍 **Industry Case Study Deep Dives:**
Learn how leading organizations leverage {topic} to drive innovation and success.

Fantastic work, hariprasadmanoj3! Your ability to translate concepts into working solutions is developing rapidly! 🎯""",
                "learning_objectives": [
                    f"Build complete, functional {topic} projects from start to finish",
                    "Apply theoretical knowledge to solve real-world problems",
                    "Develop professional project management skills",
                    "Gain hands-on experience with industry tools",
                    "Create an impressive portfolio demonstrating expertise"
                ],
                "key_concepts": [
                    "Project Development",
                    "Real-world Problem Solving",
                    "Professional Development Tools",
                    "Quality Assurance",
                    "Portfolio Building"
                ]
            },
            {
                "title": f"Advanced {topic} Techniques and Professional Mastery",
                "content": f"""Excellent progress, hariprasadmanoj3! You're ready to master the advanced techniques that distinguish expert practitioners.

🎖️ **Achieving Professional-Level Expertise:**
Here, we explore sophisticated techniques, architectural patterns, and optimization strategies used by industry leaders.

🔬 **Advanced Technical Deep Dives:**
Learn enterprise-grade design patterns, performance optimization, and security best practices.

🛡️ **Security and Reliability Engineering:**
Master comprehensive security frameworks and reliability engineering practices.

Outstanding achievement, hariprasadmanoj3! You've reached an advanced level of {topic} expertise! 🎖️""",
                "learning_objectives": [
                    f"Implement enterprise-grade {topic} architectures",
                    "Master advanced performance optimization techniques",
                    "Apply comprehensive security practices",
                    "Develop technical leadership capabilities",
                    "Design production-ready systems"
                ],
                "key_concepts": [
                    "Enterprise Architecture",
                    "Performance Engineering",
                    "Security Engineering",
                    "Technical Leadership",
                    "Production Systems"
                ]
            },
            {
                "title": f"Career Mastery and Future Growth in {topic}",
                "content": f"""🎉 Congratulations, hariprasadmanoj3! You've completed an extraordinary journey from {topic} beginner to advanced practitioner.

🏆 **Celebrating Your Remarkable Achievement:**
You've accomplished something truly significant and now possess comprehensive expertise that positions you among the top tier of {topic} professionals.

🚀 **Strategic Career Pathways:**
Explore executive and leadership tracks, technical specialization opportunities, and entrepreneurial ventures.

💼 **Building Your Professional Brand:**
Develop a world-class portfolio, create thought leadership content, and build meaningful professional networks.

🎯 **Your {topic} Legacy:**
Use your expertise to make a positive difference in the world and contribute to the advancement of the field.

The {topic} community is excited to see what you'll build and the positive impact you'll create! 🌟""",
                "learning_objectives": [
                    f"Develop a comprehensive strategic career plan leveraging {topic} expertise",
                    "Build a powerful professional brand and thought leadership presence",
                    "Create advanced specialization strategies for continued growth",
                    "Establish meaningful professional networks",
                    "Design systems for lifelong learning and advancement"
                ],
                "key_concepts": [
                    "Strategic Career Planning",
                    "Professional Brand Building",
                    "Thought Leadership",
                    "Advanced Specialization",
                    "Community Impact"
                ]
            }
        ]
        
        # Generate lessons with quizzes and videos
        for i, lesson_template in enumerate(lessons_templates):
            print(f"[2025-06-28 20:47:46] Generating lesson {i+1} for hariprasadmanoj3: {lesson_template['title']}")
            lesson = {
                **lesson_template,
                "youtube_videos": self.generate_youtube_videos(topic, lesson_template["title"]),
                "quiz": self.generate_quiz(topic, lesson_template["title"], i)
            }
            course_content["lessons"].append(lesson)
        
        print(f"[2025-06-28 20:47:46] Course content generation completed with {len(course_content['lessons'])} lessons for hariprasadmanoj3")
        return course_content

    def generate_youtube_videos(self, topic, lesson_title):
        """Generate YouTube video recommendations"""
        videos = [
            {
                "title": f"{lesson_title} - Complete Tutorial for 2025",
                "url": f"https://youtube.com/watch?v=dQw4w9WgXcQ",
                "embed_url": f"https://youtube.com/embed/dQw4w9WgXcQ",
                "channel_title": f"{topic} Academy 2025",
                "description": f"Comprehensive tutorial covering {lesson_title} with latest 2025 updates"
            },
            {
                "title": f"Practical Examples: {lesson_title}",
                "url": f"https://youtube.com/watch?v=oHg5SJYRHA0",
                "embed_url": f"https://youtube.com/embed/oHg5SJYRHA0",
                "channel_title": f"Learn {topic} Fast",
                "description": f"Hands-on practical examples for {lesson_title}"
            }
        ]
        return videos

    def generate_quiz(self, topic, lesson_title, lesson_index):
        """Generate comprehensive quiz questions for each lesson"""
        
        quiz_templates = [
            {
                "questions": [
                    {
                        "question": f"What is the primary purpose of learning {topic} in 2025?",
                        "options": [
                            f"To solve complex problems efficiently and stay competitive",
                            f"To replace all traditional methods immediately",
                            f"To make simple tasks unnecessarily complicated",
                            f"To confuse beginners with technical jargon"
                        ],
                        "correct_answer": f"To solve complex problems efficiently and stay competitive",
                        "explanation": f"{topic} is essential for solving complex problems efficiently while remaining competitive in today's technology-driven market."
                    },
                    {
                        "question": f"Which benefit does mastering {topic} provide for hariprasadmanoj3?",
                        "options": [
                            f"Significant career advancement opportunities",
                            f"Decreased logical thinking requirements",
                            f"Limited application scope",
                            f"Reduced task efficiency"
                        ],
                        "correct_answer": f"Significant career advancement opportunities",
                        "explanation": f"Mastering {topic} provides substantial career growth opportunities and enhances problem-solving capabilities."
                    }
                ]
            },
            {
                "questions": [
                    {
                        "question": f"What are the core principles of effective {topic} practice?",
                        "options": [
                            f"Systematic approach, best practices, continuous improvement",
                            f"Random experimentation and avoiding documentation",
                            f"Complex over-engineering and avoiding collaboration",
                            f"Quick fixes and minimal planning"
                        ],
                        "correct_answer": f"Systematic approach, best practices, continuous improvement",
                        "explanation": f"Effective {topic} practice is built on systematic approaches, proven best practices, and continuous improvement."
                    }
                ]
            },
            {
                "questions": [
                    {
                        "question": f"What's the most effective way to develop practical {topic} skills?",
                        "options": [
                            f"Building complete projects that solve real problems",
                            f"Only reading theoretical materials",
                            f"Avoiding challenging problems",
                            f"Working in isolation without feedback"
                        ],
                        "correct_answer": f"Building complete projects that solve real problems",
                        "explanation": f"Building real projects provides comprehensive practical experience and demonstrates problem-solving abilities."
                    }
                ]
            },
            {
                "questions": [
                    {
                        "question": f"What distinguishes advanced {topic} techniques?",
                        "options": [
                            f"Focus on scalability, performance, security, and reliability",
                            f"Ignoring performance and maintainability",
                            f"Using only basic methods without optimization",
                            f"Avoiding advanced planning and security"
                        ],
                        "correct_answer": f"Focus on scalability, performance, security, and reliability",
                        "explanation": f"Advanced {topic} techniques prioritize scalability, performance, security, and reliability for enterprise solutions."
                    }
                ]
            },
            {
                "questions": [
                    {
                        "question": f"What's the best strategy for continuous {topic} learning?",
                        "options": [
                            f"Regular practice, community participation, and personal projects",
                            f"Stop learning after formal education",
                            f"Rely only on course knowledge",
                            f"Avoid real projects and focus on theory"
                        ],
                        "correct_answer": f"Regular practice, community participation, and personal projects",
                        "explanation": f"Continuous learning through practice, community engagement, and personal projects maintains and grows expertise."
                    }
                ]
            }
        ]
        
        if lesson_index < len(quiz_templates):
            return quiz_templates[lesson_index]
        else:
            return quiz_templates[0]

@method_decorator(csrf_exempt, name='dispatch')
class CourseDetailView(View):
    def get(self, request, course_id):
        try:
            print(f"[2025-06-28 20:47:46] Fetching course details for hariprasadmanoj3, course ID: {course_id}")
            course = Course.objects.get(id=course_id)
            
            response_data = {
                'success': True,
                'course': {
                    'id': str(course.id),
                    'topic': course.topic,
                    'status': course.status,
                    'created_at': course.created_at.isoformat(),
                    'created_by': course.created_by,
                    **course.course_data
                }
            }
            
            print(f"[2025-06-28 20:47:46] Course details fetched successfully for hariprasadmanoj3")
            return JsonResponse(response_data)
            
        except Course.DoesNotExist:
            print(f"[2025-06-28 20:47:46] Course not found for hariprasadmanoj3: {course_id}")
            return JsonResponse({
                'success': False,
                'error': 'Course not found'
            }, status=404)
        except Exception as e:
            print(f"[2025-06-28 20:47:46] Error fetching course {course_id} for hariprasadmanoj3: {str(e)}")
            import traceback
            traceback.print_exc()
            return JsonResponse({
                'success': False,
                'error': 'Failed to fetch course'
            }, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class CourseListView(View):
    def get(self, request):
        try:
            print(f"[2025-06-28 20:47:46] Fetching course list for hariprasadmanoj3")
            
            # Get all courses from database
            courses = Course.objects.all().order_by('-created_at')
            total_courses = courses.count()
            
            print(f"[2025-06-28 20:47:46] Found {total_courses} courses in database")
            
            courses_data = []
            for course in courses:
                course_data = {
                    'id': str(course.id),
                    'topic': course.topic,
                    'status': course.status,
                    'created_at': course.created_at.isoformat(),
                    'created_by': course.created_by,
                    'total_lessons': course.course_data.get('total_lessons', 0) if course.course_data else 0
                }
                courses_data.append(course_data)
                print(f"[2025-06-28 20:47:46] Added course to response: {course.topic} (ID: {course.id})")
            
            print(f"[2025-06-28 20:47:46] Returning {len(courses_data)} courses for hariprasadmanoj3")
            
            return JsonResponse({
                'success': True,
                'courses': courses_data,
                'total_count': total_courses,
                'timestamp': '2025-06-28 20:47:46'
            })
            
        except Exception as e:
            print(f"[2025-06-28 20:47:46] Error fetching courses for hariprasadmanoj3: {str(e)}")
            import traceback
            traceback.print_exc()
            return JsonResponse({
                'success': False,
                'error': 'Failed to fetch courses'
            }, status=500)

@method_decorator(csrf_exempt, name='dispatch')  
class SearchCoursesView(View):
    def get(self, request):
        try:
            query = request.GET.get('q', '').strip()
            print(f"[2025-06-28 20:47:46] Searching courses for hariprasadmanoj3 with query: '{query}'")
            
            if not query:
                courses = Course.objects.all().order_by('-created_at')
            else:
                courses = Course.objects.filter(
                    topic__icontains=query
                ).order_by('-created_at')
            
            courses_data = []
            for course in courses:
                course_data = {
                    'id': str(course.id),
                    'topic': course.topic,
                    'status': course.status,
                    'created_at': course.created_at.isoformat(),
                    'created_by': course.created_by,
                    'total_lessons': course.course_data.get('total_lessons', 0) if course.course_data else 0
                }
                courses_data.append(course_data)
            
            print(f"[2025-06-28 20:47:46] Search returned {len(courses_data)} courses for hariprasadmanoj3")
            return JsonResponse({
                'success': True,
                'courses': courses_data,
                'query': query,
                'timestamp': '2025-06-28 20:47:46'
            })
            
        except Exception as e:
            print(f"[2025-06-28 20:47:46] Error searching courses for hariprasadmanoj3: {str(e)}")
            import traceback
            traceback.print_exc()
            return JsonResponse({
                'success': False,
                'error': 'Failed to search courses'
            }, status=500)