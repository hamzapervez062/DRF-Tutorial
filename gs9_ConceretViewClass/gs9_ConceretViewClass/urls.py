
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu_list/', views.StudentList.as_view()),
    path('stu_create/', views.StudentCreate.as_view()),
    path('stu_retrieve/<int:pk>/', views.StudentRetrieve.as_view()),
    path('stu_update/<int:pk>/', views.StudentUpdate.as_view()),
    path('stu_delete/<int:pk>/', views.StudentDelete.as_view()),

    path('LCStudentApi/', views.StudentListCreate.as_view()),
    path('RUStudentApi/<int:pk>/', views.StudentRetrieveUpdate.as_view()),
    path('RUDStudentApi/<int:pk>/', views.StudentRetrieveUpdateDestroy.as_view()),
]
