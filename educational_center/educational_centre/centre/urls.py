from django.urls import path, include
from centre import views

urlpatterns = [
    path('leader/', views.LeaderView.as_view()),
    path('teachers/', views.TeachersListView.as_view()),
    path('students/', views.StudentListView.as_view()),
]
