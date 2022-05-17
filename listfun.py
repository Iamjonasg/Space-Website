import json

file = open("launches.json")
launches = json.load(file)
prompt = "Falcon"
successes = 0
failures = 0
others = 0
count = 0
for ele in launches:
    if ele['rocket']['configuration']['family'] == prompt:
        count += 1
        print(ele['status']['abbrev'])
        if ele['status']['abbrev'] == 'Success':
            successes += 1

        elif ele['status']['abbrev'] == 'Failure':
            failures += 1
        else:
            others += 1
