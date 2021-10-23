import requests

r = requests.get('http://jsonplaceholder.typicode.com/posts')
print(f"status code is {r.status_code}")
print(f"response is {r.json()}")









