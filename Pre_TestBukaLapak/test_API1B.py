import requests

url = 'https://jsonplaceholder.typicode.com/posts'
expected = {'title': 'recommendation','body':'motocycle','userId':12}

bl = requests.post(url, data = expected)

for i in bl.json().items():
    if i[0] in list(expected):
        print (expected[i[0]])
        if i[1] == expected[i[0]]:
            print ('true')
        else:
            print('false')