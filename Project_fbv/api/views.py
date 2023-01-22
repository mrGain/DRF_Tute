from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer
# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def studentView(request,id=None):
    if request.method == "GET":
        id = id
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data, status=status.HTTP_200_OK)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Created","data":request.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    if request.method == "PUT":
        id = id
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Updated","data":request.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PATCH":
        id = id
        try:
            stu = Student.objects.get(id=id)
        except:
            return Response({"msg":"Data Not Found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(stu,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Updated","data":request.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        id = id
        try:
            stu = Student.objects.get(id=id)
        except:
            return Response({"msg":"Data Not Found"}, status=status.HTTP_404_NOT_FOUND)

        stu.delete()
        return Response({"msg":"Data Deleted"}, status=status.HTTP_204_NO_CONTENT)   