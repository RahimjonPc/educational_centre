from django.db import models
from django.contrib.auth.models import User
from users.models import *


class MarkOfStudent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    mark = models.IntegerField()
    academic_performance = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return str(self.user)
