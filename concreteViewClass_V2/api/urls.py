from django.urls import path 

from .views import StudentListCreate, StudentRetrieveUpdateDestroy


urlpatterns = [
    path('student/', StudentListCreate.as_view()),
    path('student/<int:pk>/', StudentRetrieveUpdateDestroy.as_view()),
]