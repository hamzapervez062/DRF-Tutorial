import requests 
import json

URL = "http://127.0.0.1:8000/stu_api/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    headers = {'content-type': 'application/json'}
    json_data = json.dumps(data) #converts data into json
    # print('json', json_data , 'data', data)
    r = requests.get(url = URL,headers=headers , data = json_data) # get is used to fetch data
    data = r.json()  
    print(data)

get_data()

def post_data():
    data = {
        'name': 'alia',
        'roll': 22,
        'city': 'LA'
    }
    headers = {'content-type': 'application/json'} 
    json_data = json.dumps(data) #converts data into json
    r = requests.post(url = URL, headers = headers ,data = json_data)  # post is used to send data
    data = r.json()  
    print(data)

# post_data()

def update_data(id):

    data = {
        'id': id,
        'name': 'ajr',
        'roll': 2,
    }
    headers = {'content-type': 'application/json'}
    json_data = json.dumps(data) #converts data into json
    r = requests.put(url = URL,headers=headers ,data = json_data)  # put is used to update data
    data = r.json()  
    print(data)

# update_data(1)

def delete_data(id):
    data = {
        'id': id
    }
    headers = {'content-type': 'application/json'}
    json_data = json.dumps(data) #converts data into json
    r = requests.delete(url = URL, headers=headers , data = json_data)  # delete is used to delete data
    data = r.json()  
    print(data)

# delete_data(1)