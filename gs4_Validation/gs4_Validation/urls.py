from django.contrib import admin
from django.urls import path
from api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_api/', views.student_api),
    #CBV
    # path('student_apicbv/', views.STUDENTAPIVIEW.as_view()),
]
