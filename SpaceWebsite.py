import requests

response = requests.get("https://lldev.thespacedevs.com/2.2.0/launch/?limit=99")
print(response.status_code)
raw = response.json()
print(raw)
results = raw["results"]
print(len(results))