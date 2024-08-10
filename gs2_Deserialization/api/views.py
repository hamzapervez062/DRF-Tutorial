from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body # The request body containing the JSON data is received in the request.
        print(json_data)
        stream = io.BytesIO(json_data) # This JSON data is in bytes, so it is first converted to a stream using BytesIO. This stream can now be parsed.
        print(stream)
        pythondata = JSONParser().parse(stream) # we parse a stream into Python native datatypes...
        print(pythondata)
        # then we restore those native datatypes into a dictionary of validated data.
        serializer = StudentSerializer(data = pythondata) # Deserialize the native Python datatypes into a dictionary of validated data using the serializer:
        print(serializer)
        if serializer.is_valid(): # The serializer.is_valid() method validates if the data structure and data types match the serializer fields.
            serializer.save()     # Calling .save() will either create a new instance.
            res = {'msg':'Data Created'}
            json_data = JSONRenderer().render(res) # JSONRenderer().render(res) is used to convert res into json data.
            return HttpResponse(json_data, content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')






