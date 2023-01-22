from django.urls import path
from .views import StudentList, StudentDetail
urlpatterns = [
    path('student/', StudentList.as_view(), name='student_list'),
    path('student/<int:pk>/', StudentDetail.as_view(), name='student_detail'),
]
