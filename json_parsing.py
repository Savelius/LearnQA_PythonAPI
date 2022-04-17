import requests

response = requests.post("https://playground.learnqa.ru/api/something")
print(response.status_code)
print(response.text)
