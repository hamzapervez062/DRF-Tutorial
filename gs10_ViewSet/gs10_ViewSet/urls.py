
from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

# Create a router 
router = DefaultRouter()

# Register StudentViewSet with router
router.register('studentapi', views.StudentViewSet, basename='student') # it will work for all actions like list, create, retrieve, update, delete

# router.register('studentapi/<int:pk>', views.StudentViewSet, basename='student') 
#as we used to make  url like this for retrieve, update, delete, 
# but now dont need that, only single url will work

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))

]
