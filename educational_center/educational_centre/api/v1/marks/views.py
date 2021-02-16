from rest_framework import generics
from marks.models import MarkOfStudent
from .serializers import MarkCRUDSerializer

class MarkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MarkOfStudent
    serializer_class = MarkCRUDSerializer


class MarksListView(generics.ListAPIView):
    model = MarkOfStudent
    queryset = MarkOfStudent.objects.all()
    serializer_class = MarkCRUDSerializer

    def get_queryset(self):
        marks = MarkOfStudent.objects.all()
        if self.request.GET.get('student'):
            student_id = self.request.GET.get('student')
            return MarkOfStudent.objects.filter(user__id=student_id)
        

    