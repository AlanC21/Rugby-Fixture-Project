import requests

url = "https://v1.rugby.api-sports.io/"

payload={}
headers = {
  'x-rapidapi-key': 'd74a21af68fba812a78cb2974b11af00',
  'x-rapidapi-host': 'v1.rugby.api-sports.io'
}

response = requests.get(url, headers=headers)
