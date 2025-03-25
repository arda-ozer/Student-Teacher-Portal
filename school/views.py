from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile, Student, Grade
from django.contrib import messages

@login_required
def home(request):
    profile = Profile.objects.get(user=request.user)
    if profile.user_type == 'teacher':
        students = Student.objects.all()  # Get all students
        context = {'students': students}
        return render(request, 'school/teacher_home.html', context)
    elif profile.user_type == 'student':
        student = Student.objects.get(profile=profile)
        try:
            grade = Grade.objects.get(student=student)  # Get student's grade
        except Grade.DoesNotExist:
            grade = None  # If no grade exists, set to None
        context = {'student': student, 'grade': grade}
        return render(request, 'school/student_home.html', context)
    else:
        return redirect('login')

@login_required
def add_grade(request, student_id):
    profile = Profile.objects.get(user=request.user)
    if profile.user_type != 'teacher':
        return redirect('home')  # Only teachers can add grades
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        score = request.POST.get('score')
        Grade.objects.update_or_create(student=student, defaults={'score': score})
        messages.success(request, f"Grade successfully added for {student.name}!")
        return redirect('home')
    return render(request, 'school/add_grade.html', {'student': student})

@login_required
def edit_grade(request, student_id):
    profile = Profile.objects.get(user=request.user)
    if profile.user_type != 'teacher':
        return redirect('home')  # Only teachers can edit grades
    student = get_object_or_404(Student, id=student_id)
    grade = get_object_or_404(Grade, student=student)
    if request.method == 'POST':
        score = request.POST.get('score')
        grade.score = score
        grade.save()
        messages.success(request, f"Grade successfully updated for {student.name}!")
        return redirect('home')
    return render(request, 'school/edit_grade.html', {'student': student, 'grade': grade})