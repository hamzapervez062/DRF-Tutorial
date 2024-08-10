import requests 
import json

URL = "http://127.0.0.1:8000/student_apicbv/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data) #converts data into json
    # print('json', json_data , 'data', data)
    r = requests.get(url = URL, data = json_data) # get is used to fetch data
    data = r.json()  
    print(data)

# get_data(1)

def post_data():
    data = {
        'name': 'Saira',
        'roll': 2006,
        'city': 'LA'
    }
    json_data = json.dumps(data) #converts data into json
    r = requests.post(url = URL, data = json_data)  # post is used to send data
    data = r.json()  
    print(data)

# post_data()

def update_data(id):

    data = {
        'id': id,
        'name': 'jr',
        'roll': 2022,
    }
    json_data = json.dumps(data) #converts data into json
    r = requests.put(url = URL, data = json_data)  # put is used to update data
    data = r.json()  
    print(data)

# update_data(1)

def delete_data(id):
    data = {
        'id': id
    }
    json_data = json.dumps(data) #converts data into json
    r = requests.delete(url = URL, data = json_data)  # delete is used to delete data
    data = r.json()  
    print(data)

delete_data(1)