from rest_framework import serializers
from marks.models import MarkOfStudent

class MarkCRUDSerializer(serializers.ModelSerializer):

    class Meta:
        model = MarkOfStudent
        fields = ('id', 'mark', 'academic_performance')