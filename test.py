import requests
import json

response = requests.get("https://lldev.thespacedevs.com/2.2.0/launch/previous/")
results = []
print(response.status_code)
raw = response.json()
count = raw["count"]
print(count)
results.extend(raw["results"])


with open("launches.json", 'w') as file:
    json.dump(results, file, indent=2)


