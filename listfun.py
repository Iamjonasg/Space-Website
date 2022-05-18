import json
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker

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
            if ele['status']['abbrev'] == 'Success':
                years[year][0] += 1

            elif ele['status']['abbrev'] == 'Failure':
                years[year][1] += 1

            else:
                years[year][2] += 1
            years[year][3] += 1
        else:
            if ele['status']['abbrev'] == 'Success':
                years[year] = [1, 0, 0, 1]

            elif ele['status']['abbrev'] == 'Failure':
                years[year] = [0, 1, 0, 1]

            else:
                years[year] = [0, 0, 1, 1]


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

for ele in newyears:
    if ele not in years:
        years[ele] = [0, 0, 0, 0]

years = dict(sorted(years.items()))
print(years)

results = []
labels = []
colors = []
if successes != 0:
    results.append(successes)
    labels.append("Success")
    colors.append('#22A721')
if failures != 0:
    results.append(failures)
    labels.append("Failure")
    colors.append('#A7171A')
if others != 0:
    results.append(others)
    labels.append("Other")
    colors.append('grey')


plt.rcParams['font.size'] = '7'
fig1 = plt.figure(figsize=(10,3))

plot1 = fig1.add_subplot(121)
plot2 = fig1.add_subplot(122)
fig1.suptitle(prompt + " rocket family stats", fontsize=14)
plot1.pie(results, labels=labels, colors=colors, autopct=lambda x: f'{x:.1f}%',)
plot1.axis('equal')

labelsbar = list(years.keys())
for i in range(len(labelsbar)):
    labelsbar[i] = int(labelsbar[i])


successes_per_year = []
failures_per_year = []
others_per_year = []
for ele in years:
    successes_per_year.append(years[ele][0])
for ele in years:
    failures_per_year.append(years[ele][1])
for ele in years:
    others_per_year.append(years[ele][2])
successes_per_year = np.array(successes_per_year)
failures_per_year = np.array(failures_per_year)
others_per_year = np.array(others_per_year)

plt.title("Launches per year")
plot2.bar(labelsbar, others_per_year, label='Other', color='grey' )
plot2.bar(labelsbar, failures_per_year, bottom=others_per_year, label='Failure', color='#A7171A' )
plot2.bar(labelsbar, successes_per_year, bottom=failures_per_year+others_per_year, label='Success', color='#22A721' )

if len(labelsbar) > 20:

    myLocator = mticker.MultipleLocator(5)
    plot2.xaxis.set_major_locator(myLocator)
elif len(labelsbar) > 10:
    myLocator = mticker.MultipleLocator(3)
    plot2.xaxis.set_major_locator(myLocator)
else:
    myLocator = mticker.MultipleLocator(1)
    plot2.xaxis.set_major_locator(myLocator)
start, end = plot2.get_ylim()


max = 0
for ele in years:
    current = years[ele][3]

    if current > max:
        max = current
if max < 10:
    plot2.yaxis.set_ticks(np.arange(start, end, 1))

plot2.legend()
plt.show()




