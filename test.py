import requests

BASE = "http://127.0.0.1:5000/"
# print(url)
# url2 = url + "tim/19"
# url4 = BASE + "video/1", {"likes": 10}
# url3 = BASE + "ben"
# response = requests.get(url)
# print(response.json())

response = requests.put(BASE + "video/1", {"likes": 10})
print(response.json())
# response = requests.get(url3)
# print(response.json())
