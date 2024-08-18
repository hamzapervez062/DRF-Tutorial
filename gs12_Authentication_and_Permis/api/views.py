from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, BasePermission


# Create your views here.
# https://medium.com/@yashnarsamiyev2/authentication-permissions-in-django-rest-framework-e29fe0080d0e

class ModelStudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer 
    # authentication_classes = [BasicAuthentication] # it is use for authentication before accessing the api
    # permission_classes = [IsAuthenticated]


# class ModelStudentViewSet2(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer 
#     authentication_classes = [BasicAuthentication] 
#     permission_classes = [AllowAny] # override the global permission


#------------------------------------Session Authentication------------------------------------------------------------

# https://blog.devgenius.io/session-authentication-in-django-rest-framework-5e3f6fb44c59

class ModelStudentViewSet3(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer 
    authentication_classes = [SessionAuthentication] 
    # permission_classes = [IsAuthenticated]
    # permission_classes = [DjangoModelPermissions]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]



#---------------------------------------------------------------------------------------------------------------------


# How Session Authentication is different from Basic Authentication?

# In the basic authentication we need to send the username and password for every request.
# In the session authentication we will send username and password at initial request. 
# Then from server response we get the session id which stores in browser and gonna use that for requests.


#------------------------------------Custom Permission------------------------------------------------
# ------------https://testdriven.io/blog/custom-permission-classes-drf/

class CutomModelStudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer 
    authentication_classes = [SessionAuthentication] 
    class MyPermission(BasePermission):
        def has_permission(self, request, view):
            if request.method == 'GET':
                return True # user can access the api
            return False

    permission_classes = [MyPermission]