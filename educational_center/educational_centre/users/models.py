from django.db import models
from django.contrib.auth.models import User
from datetime import date
from cources.models import *
from events.models import *
from cources.models import Courses


class LeaderProfile(models.Model):
    user = models.OneToOneField(User, related_name='leader', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='leader_poster')
    sex = models.CharField(max_length=10, blank=True)
    birthday = models.DateField(blank=True, null=True)
    phone = models.IntegerField()
    email = models.EmailField(max_length=150)

    def __str__(self):
        return str(self.user)


class Teacher(models.Model):
    user = models.OneToOneField(User, related_name='teacher', on_delete=models.CASCADE)
    cources = models.ManyToManyField(Courses)
    image = models.ImageField(upload_to='teacher_poster', blank=True, null=True)
    bio = models.CharField(max_length=250)
    experience = models.CharField(max_length=250)
    sex = models.CharField(max_length=10)
    birthday = models.DateField()
    phone = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user)


class Student(models.Model):
    user = models.OneToOneField(User, related_name='student', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='student_poster', blank=True, null=True)
    sex = models.CharField(max_length=10)
    birthday = models.DateField()
    phone = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.user)


class StudentGroup(models.Model):
    name_of_group = models.CharField(max_length=200)
    teacher_of_group = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students_in_the_group = models.ManyToManyField(Student)

    def __str__(self):
        return str(self.name_of_group)