
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views

# Create a router
router = routers.DefaultRouter()

# Register StudentViewSet with router
router.register('studentapi', views.ModelStudentViewSet, basename='student') # for basic authentication	
router.register('sessionapi', views.ModelStudentViewSet3, basename='session_api') # for session authentication	
router.register('custom', views.CutomModelStudentViewSet, basename='cuatom') # for custom permission


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')) # for session authentication for login

]
