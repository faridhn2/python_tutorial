import requests
print(requests.get('https://cdn.snappfood.ir/200x201/cdn/81/57/0/vendor/629bb658befe9.jpeg'))
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'  }
print(requests.get('https://cdn.snappfood.ir/200x201/cdn/81/57/0/vendor/629bb658befe9.jpeg',
headers=header))

