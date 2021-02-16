from rest_framework import serializers
from events.models import Events

class EventsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Events
        fields = ("id", "day", "start", "finish", "teacher", "student_group", "cource",)