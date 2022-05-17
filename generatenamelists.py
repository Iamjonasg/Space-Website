import json
6403
file = open("launches.json")
launches = json.load(file)
rocketnames = []
rocketfamilies = []

i = 0
while i < len(launches):
    currentname = launches[i]['rocket']['configuration']['name']
    currentfamily = launches[i]['rocket']['configuration']['family']
    if currentname not in rocketnames:
        rocketnames.append(currentname)
    if currentfamily not in rocketfamilies:
        rocketfamilies.append(currentfamily)
    i+=1


with open("names.json", 'w') as file:
    json.dump(rocketnames, file, indent=1)

with open("families.json", 'w') as file:
    json.dump(rocketfamilies, file, indent=1)