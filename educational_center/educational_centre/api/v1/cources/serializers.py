from rest_framework import serializers
from cources.models import Courses

class CoursesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Courses
        fields = ('id', 'name', 'description', 'amount_of_lessons', 'price')