import json
import matplotlib.pyplot as plt


file = open("launches.json")
launches = json.load(file)
prompt = "Saturn"
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


newyears = list(years.keys())



for i in range(len(newyears)):

    newyears[i] = int(newyears[i])


newyears = list(reversed(newyears))


def fill_in_numbers(lst):
    i=0
    while True:
        if lst[i+1] != lst[i] + 1:
             lst.insert(i+1, lst[i]+1)
        i+=1
        if lst[-1] - lst[i]== 1:
            break
    return lst


fill_in_numbers(newyears)


for i in range(len(newyears)):

    newyears[i] = str(newyears[i])
print(newyears)
for ele in newyears:
    if ele not in years:
        years[ele] = 0

years = dict(sorted(years.items()))


results = [successes, failures, others]
labels = ["Success", "Failure", "Other"]
colors = ['green', 'red', 'grey']


plt.rcParams['font.size'] = '5'
fig1 = plt.figure(figsize=(10,3))
plot1 = fig1.add_subplot(121)
plot2 = fig1.add_subplot(122)
plot1.pie(results, labels=labels, colors=colors, autopct=lambda x: f'{x:.1f}%',)
plot1.axis('equal')

plot2.bar(years.keys(), years.values())
plt.show()



print(years)
print(successes)
print(failures)
print(others)
print(successes/(successes+failures)*100)
