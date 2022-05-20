import json
6403
file = open("launches.json")
launches = json.load(file)
rocketnames = []
rocketfamilies = []
rocketfullnames = []
agencies = []
i = 0
while i < len(launches):
    currentname = launches[i]['rocket']['configuration']['name']
    currentfamily = launches[i]['rocket']['configuration']['family']
    currentfullname = launches[i]['rocket']['configuration']['full_name']
    currentagency = launches[i]['launch_service_provider']['name']
    if currentname not in rocketnames:
        rocketnames.append(currentname)
    if currentfamily not in rocketfamilies:
        rocketfamilies.append(currentfamily)
    if currentfullname not in rocketfullnames:
        rocketfullnames.append(currentfullname)
    if currentagency not in agencies:
        agencies.append(currentagency)
    i+=1


with open("names.json", 'w') as file:
    json.dump(rocketnames, file, indent=1)

with open("families.json", 'w') as file:
    json.dump(rocketfamilies, file, indent=1)

with open("fullnames.json", 'w') as file:
    json.dump(rocketfullnames, file, indent=1)

with open("agencies.json", 'w') as file:
    json.dump(agencies, file, indent=1)