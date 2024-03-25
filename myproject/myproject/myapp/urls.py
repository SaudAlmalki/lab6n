from django.urls import path
from .views import students, courses, details

urlpatterns = [
    path('students/', students, name='students'),
    path('courses/', courses, name='courses'),
    path('details/<int:student_id>/', details, name='details'),
]