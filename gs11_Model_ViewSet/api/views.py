from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action


# Create your views here.
# What is ModelViewSet?
# ModelViewSet inherits from GenericViewSet and includes implementations for the basic CRUD actions using the appropriate serializer and model. 


# Medium: https://blog.devgenius.io/viewset-and-modelviewset-in-drf-690ab99a7afa

class ModelStudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer 

# these 3 above lines perform the CRUD operations

class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset= Student.objects.all()
    serializer_class = StudentSerializer