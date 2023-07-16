import requests

url = "https://yh-finance-complete.p.rapidapi.com/investp"

querystring = {"conversion":"usd-btc","period":"P1W"}

headers = {
	"X-RapidAPI-Key": "b41e4931f0msh423b87aae44f63fp1e52ebjsnb67509559816",
	"X-RapidAPI-Host": "yh-finance-complete.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.text)