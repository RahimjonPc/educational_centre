from rest_framework import serializers
from .models import LeaderProfile, Teacher, Student, Courses, Events


class LeaderSerializer(serializers.ModelSerializer):

    class Meta:
        model = LeaderProfile
        fields = ("image", "sex", "age", "phone", "email")


class TeacherListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ("image", "bio", "experience", "sex", "age", "phone", "email")


class StudentListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = ("image", "sex", "age", "phone", "email")