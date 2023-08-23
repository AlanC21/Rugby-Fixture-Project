import requests

url = "https://rugby-live-data.p.rapidapi.com/fixtures/1272/2024"

headers = {
	"X-RapidAPI-Key": "cdeaaf4e02mshffcfe442dc1cba2p14985ajsndb3fa3629176",
	"X-RapidAPI-Host": "rugby-live-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
