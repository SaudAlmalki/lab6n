from django.shortcuts import render, redirect
from .models import Student, Course

def students(request):
    if request.method == 'POST':
        return redirect('students')
    else:
        students_list = Student.objects.all()
        return render(request, 'students.html', {'students': students_list})

def courses(request):
    if request.method == 'POST':
        return redirect('courses')
    else:
        courses_list = Course.objects.all()
        return render(request, 'courses.html', {'courses': courses_list})

def details(request, student_id):
    student = Student.objects.get(pk=student_id)
    available_courses = Course.objects.exclude(students=student)
    return render(request, 'details.html', {'student': student, 'available_courses': available_courses})
