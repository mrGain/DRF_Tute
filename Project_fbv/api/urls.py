from django.urls import path

from . import views 

urlpatterns = [
    path('student/', views.studentView, name='student'),
    path('student/<int:id>', views.studentView, name='student'),
    
]