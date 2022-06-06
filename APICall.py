import requests
import json

response = requests.get("https://lldev.thespacedevs.com/2.2.0/launch/previous/")
results = []
print(response.status_code)
raw = response.json()
count = raw["count"]
print(count)
offset = 0
while offset < count:
    url = "https://lldev.thespacedevs.com/2.2.0/launch/previous/?limit=100&offset="+str(offset)
    print(url)
    response = requests.get(url)
    raw = response.json()
    results.extend(raw["results"])
    offset += 100

with open("launches.json", 'w') as file:
    json.dump(results, file, indent=2)


