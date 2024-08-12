from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu_api/', views.student_api),
    #
    path('brw_student_api/', views.brw_student_api),
    path('brw_student_api/<int:pk>/', views.brw_student_api),
]
