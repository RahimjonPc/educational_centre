from rest_framework import generics, permissions
from events.models import Events
from .serializers import EventsListSerializer


class EventsListView(generics.ListAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsListSerializer

    
    def get_queryset(self):
        events = Events.objects.all()
        if self.request.GET.get('teacher'):
            teacher_id = self.request.GET.get('teacher')
            events = Events.objects.filter(teacher__id = teacher_id)
        else:
            return
            
            

        if self.request.GET.get('student_group'):
            student_group_id = self.request.GET.get('student_group')
            events = Events.objects.filter(student_group__id=student_group_id)

        return events

        


class EventsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Events
    serializer_class = EventsListSerializer