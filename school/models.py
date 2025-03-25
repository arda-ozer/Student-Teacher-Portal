from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    USER_TYPE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.user_type}"

class Student(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    branch = models.CharField(max_length=50)  # For example, subject information
    experience_years = models.PositiveIntegerField(default=0)  # Years of experience

    def __str__(self):
        return f"{self.profile.user.username} - {self.branch}"

class Grade(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='grade')
    score = models.PositiveIntegerField(default=0)  # Score (can be a value between 0-100)

    def __str__(self):
        return f"{self.student.name} - {self.score}"