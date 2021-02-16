from django.contrib import admin
from .models import LeaderProfile, Teacher, Student, StudentGroup

admin.site.register(LeaderProfile)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(StudentGroup)