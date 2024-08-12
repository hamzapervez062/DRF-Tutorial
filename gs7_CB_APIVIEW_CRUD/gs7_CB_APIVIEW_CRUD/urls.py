from django.contrib import admin
from django.urls import path
from api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuapi/', views.Student_api.as_view()),
    path('stuapi/<int:pk>', views.Student_api.as_view()),
]