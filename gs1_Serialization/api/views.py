from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

# Model object- Single Student Data
def student_detail(request):
    stu = Student.objects.get(pk = 1)
    serializer = StudentSerializer(stu,many=False)
    print(serializer.data)

    json_data = JSONRenderer().render(serializer.data)

    return HttpResponse(json_data, content_type = 'application/json')

# Queryset- All Student Data
def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu,many=True)

    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type = 'application/json')

    return JsonResponse(serializer.data, safe=False)
