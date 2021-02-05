
import requests
# import json

response = requests.get('https://jsonplaceholder.typicode.com/posts')
print(response.status_code)
jsonResponse = response.json()
data = response.json()

def test_id():
    # print(type(data[0]['id']) is int)
    for i in range(len(data)):
        assert(isinstance((data[i]['id']),int))
        print("true")

def test_title():
    # print(type(data[0]['title']) is str)
    for i in range(len(data)):
        assert (isinstance((data[i]['title']), str))
        print("true")

def test_body():
    # print(type(data[0]['title']) is str)
    for i in range(len(data)):
        assert (isinstance((data[i]['body']), str))
        print("true")

def test_userId():
    # print(type(data[0]['title']) is str)
    for i in range(len(data)):
        assert (isinstance((data[i]['userId']), int))
        print("true")
