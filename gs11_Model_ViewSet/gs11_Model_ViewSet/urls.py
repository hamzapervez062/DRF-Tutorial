
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views

# Create a router
router = routers.DefaultRouter()

# Register StudentViewSet with router
router.register('studentapi', views.ModelStudentViewSet, basename='student')
router.register('readonlystudentapi', views.StudentReadOnlyModelViewSet, basename='rdonlystudent') # only for list and retrieve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
