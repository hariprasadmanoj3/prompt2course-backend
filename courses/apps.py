from django.apps import AppConfig

class CoursesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'courses'
    verbose_name = "Course Management"
    
    def ready(self):
        # Import any signals here if needed
        pass