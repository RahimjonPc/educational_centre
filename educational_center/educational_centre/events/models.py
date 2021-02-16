from django.db import models
from django.contrib.auth.models import User
from datetime import date
# from users.models import Teacher, Student
from cources.models import *


class Events(models.Model):
    day = models.DateField()
    start = models.TimeField()
    finish = models.TimeField()
    teacher = models.ForeignKey("users.Teacher", on_delete=models.CASCADE)
    student_group = models.ForeignKey("users.StudentGroup", on_delete=models.CASCADE)
    cource = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cource)