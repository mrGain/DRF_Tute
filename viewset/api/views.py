from django.shortcuts import render
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets


class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        stu = Student.objects.all()
        serilizer = StudentSerializer(stu, many=True)
        return Response(serilizer.data)

    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serilizer = StudentSerializer(stu)
            return Response(serilizer.data)

    def create(self, request):
        serilizer = StudentSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({"msg": "DataCreated"}, status=status.HTTP_201_CREATED)
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        id = pk 
        stu = Student.objects.get(id=id)
        serilizer = StudentSerializer(stu, data= request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({"msg":"Complete data updated"})
        return Response(serilizer.errors, status= status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request, pk):
        id = pk
        stu = Student.object.get(pk = id)
        serilizer = StudentSerializer(stu, data=request.data, partial= True)
        if serilizer.is_valid():
            serilizer.save()
            return Response({"msg":"partial Data Update"})
        return Response(serilizer.errors)

    def destroy(self, request, pk):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({"msg":"Data Deleted"})
    
