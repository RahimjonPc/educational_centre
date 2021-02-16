from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions

from .models import LeaderProfile, Teacher, Student, Courses, Events, TeacherPersonalAccount, LeaderPersonalAccount, StudentPersonalAccount, MarkOfStudent
from .serializers import LeaderSerializer, TeacherListSerializer, StudentListSerializer


class LeaderView(APIView):
    def get(self, request):
        leader = LeaderProfile.objects.all()
        serializer = LeaderSerializer(leader, many=True)
        return Response(serializer.data)


class TeachersListView(generics.ListAPIView):
        queryset = Teacher.objects.all()
        serializer_class = TeacherListSerializer
        permission_classes = [permissions.IsAuthenticated]


class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer
    permission_classes = [permissions.IsAuthenticated]