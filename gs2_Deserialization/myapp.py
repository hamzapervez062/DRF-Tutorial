import requests 
import json

URL = "http://127.0.0.1:8000/stu_add/"
python_data = {
    'name' : 'Saira',
    'roll': 2006,
    'city': 'LA'
}

json_data = json.dumps(python_data)
r = requests.post(url = URL, data = json_data) #post is used to send data
data = r.json()
print(data)