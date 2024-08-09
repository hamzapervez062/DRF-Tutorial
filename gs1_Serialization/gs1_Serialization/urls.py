from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu_api/', views.student_detail),
    path('stu_list/', views.student_list),
]
