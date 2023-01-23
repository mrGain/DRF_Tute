from django.urls import path 

from .views import StudentList,StudentCreate,StudentRetrieve, StudentUpdate,StudentDestroy ,StudentListCreate, StudentRetrieveUpdate, StudentRetrieveDestroy, StudentRetrieveUpdateDestroy

urlpatterns = [
    # path('student/', StudentList.as_view(), name='student_list'),
    # path('student/', StudentCreate.as_view(), name='student_list'),
    # path('student/<int:pk>/', StudentRetrieve.as_view(), name='student_retrieve'),
    # path('student/<int:pk>/', StudentUpdate.as_view(), name='student_update'),
    # path('student/<int:pk>/', StudentDestroy.as_view()),

    # combined classes goes here
    path('student/', StudentListCreate.as_view(), name='student_list_create'),
    # path('student/<int:pk>/', StudentRetrieveUpdate.as_view(), name='student_retrieve_update'),
    # path('student/<int:pk>/', StudentRetrieveDestroy.as_view(), name='student_retrieve_destroy'),
    path('student/<int:pk>/', StudentRetrieveUpdateDestroy.as_view(), name='student_retrieve_update_destroy'),
]