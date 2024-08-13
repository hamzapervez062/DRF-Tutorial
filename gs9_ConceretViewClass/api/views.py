from django.shortcuts import render
from .models import Student
from .serilizers import StudentSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView

# Create your views here.

# https://medium.com/the-andela-way/creating-a-djangorest-api-using-djangorestframework-part-2-1231fe949795

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDelete(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
