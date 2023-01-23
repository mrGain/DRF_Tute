from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView,UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView

from .models import Student
from .serializers import StudentSerializer
# Create your views here.
# ListAPIView to List all Student
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# CreateAPIView to Create a Student
class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# RetrieveAPIView to Retrieve a single student
class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer    

# UpdateAPIView to Update a single student
class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# DestroyAPIView to Delete a single student
class StudentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# Combined classes goes here

# ListCreateAPIView for get and post request
class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# RetrieveUpdateAPIView to get a single data and Update data
class StudentRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer 

# RetrieveDestroyAPIView to get and delete a data 
class StudentRetrieveDestroy(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer    

# RetrieveUpdateDestroyAPIView to get, update and delete a data
class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer