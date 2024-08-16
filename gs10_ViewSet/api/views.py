from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action


# Create your views here.
# What is ViewSet?
# ViewSet is a higher-level abstraction that combines multiple actions (such as list, create, retrieve, update, and destroy) into a single class. 
# It is designed to handle common patterns with minimal boilerplate code.

# Medium: https://blog.devgenius.io/viewset-and-modelviewset-in-drf-690ab99a7afa

class StudentViewSet(ViewSet):
    def list(self, request):
        print("-------list-----------")
        print(self.action)
        print(self.basename)
        print(self.detail)
        print(self.kwargs)
        print(self.name)
        print(self.suffix)
        print(self.description)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def create(self, request):
        print("-------create-----------")
        print(self.action)
        print(self.basename)
        print(self.detail)
        print(self.kwargs)
        print(self.name)
        print(self.suffix)
        print(self.description)
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def retrieve(self, request, pk=None):
        print("-------retrieve-----------")
        print(self.action)
        print(self.basename)
        print(self.detail)
        print(self.kwargs)
        print(self.name)
        print(self.suffix)
        print(self.description)
        if pk is not None:
            stu = Student.objects.get(id=pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        return Response({"msg":"retrieve"})

    def update(self, request, pk=None):
        print("update")
        if pk is not None:
            stu = Student.objects.get(id=pk)
            serializer = StudentSerializer(stu, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors)

    def partial_update(self, request, pk=None):
        print("partial_update")
        if pk is not None:
            stu = Student.objects.get(id=pk)
            serializer = StudentSerializer(stu, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response({"msg":"partial_update"})

    def destroy(self, request, pk=None):
        print("destroy")
        if pk is not None:
            stu = Student.objects.get(id=pk)
            stu.delete()
            return Response({"msg":"destroy"})
        return Response({"msg":"destroy"})
