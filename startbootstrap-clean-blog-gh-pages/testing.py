import requests
from pprint import pprint

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
data = response.json()
pprint(data)


