import json

file = open("launches.json")
launches = json.load(file)
prompt = "Falcon"
successes = 0
failures = 0
others = 0
count = 0
years = {}
for ele in launches:
    if ele['rocket']['configuration']['family'] == prompt:
        count += 1

        if ele['status']['abbrev'] == 'Success':
            successes += 1

        elif ele['status']['abbrev'] == 'Failure':
            failures += 1
        else:
            others += 1

        window = str(ele['window_end'])
        year = window.partition("-")[0]
        if year in years:
            years[year] += 1
        else:
            years[year] = 1

print(years)
print(successes)
print(failures)
print(others)


print(successes/(successes+failures)*100)
