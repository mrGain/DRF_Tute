from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Student
from .serializers import StudentSerializer

# Create your views here.
class StudentList(APIView):
    def get(self, request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetail(APIView):
    def get_object(self, id):
        try:
            return Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({'msg': 'Data Not Found'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        stu = self.get_object(pk)
        serializer = StudentSerializer(stu)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        stu = self.get_object(pk)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk):
        stu = self.get_object(pk)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'}, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, pk):
        stu = self.get_object(pk)
        stu.delete()
        return Response({'msg': 'Data Deleted'}, status=status.HTTP_204_NO_CONTENT)        
        