import requests
response = requests.get('https://api.ipify.org/')
print(response.text)
response = requests.get('https://api.ipify.org?format=json')
# js = response.text
json_data = response.json()
print(type(json_data))
print(json_data)
print(json_data['ip'])
