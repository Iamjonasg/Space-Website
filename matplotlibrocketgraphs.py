import json
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker

file = open("launches.json")
launches = json.load(file)


def fill_in_numbers(lst):
    inc = 0
    while True:
        if len(lst) <= 1:
            break
        if lst[-1] - lst[inc] == 1:
            break
        if lst[inc + 1] != lst[inc] + 1:
            lst.insert(inc + 1, lst[inc] + 1)
        inc += 1

    return lst


def generate_graph(graphtype, prompt, start=False):

    successes = 0
    failures = 0
    others = 0
    count = 0
    years = {}

    if start:

        for ele in launches:
            if ele['rocket']['configuration'][graphtype].startswith(prompt):
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
    else:

        for ele in launches:

            if ele['rocket']['configuration'][graphtype] == prompt:
                
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

    newyears = sorted(newyears)

    fill_in_numbers(newyears)

    for i in range(len(newyears)):

        newyears[i] = str(newyears[i])

    for ele in newyears:
        if ele not in years:
            years[ele] = [0, 0, 0, 0]

    years = dict(sorted(years.items()))

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

    plt.rcParams['font.size'] = '9'

    labelsbar = list(years.keys())
    for i in range(len(labelsbar)):
        labelsbar[i] = int(labelsbar[i])



    fig1 = plt.figure(figsize=(10, 3))
    plot2 = fig1.add_subplot(111)



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

    plt.title("Launches per year: " + prompt + " rockets")

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




    maxvalue = 0
    for ele in years:
        current = years[ele][3]

        if current > maxvalue:
            maxvalue = current
    if maxvalue < 10:
        plot2.yaxis.set_ticks(np.arange(start, end+1, 1))

    plot2.legend(bbox_to_anchor=(1,1), loc="upper left", fontsize=8)
    plt.ylim(top=maxvalue+1)
    filename = str(graphtype+"_" + prompt)
    filename = filename.replace("/", "_")
    plt.savefig("Graphs/"+filename + ".png", dpi=600)
    
    plt.show()


def generate_agency_graph(prompt, start=False):

    successes = 0
    failures = 0
    others = 0
    count = 0
    years = {}

    if start:

        for ele in launches:
            if ele['launch_service_provider']['name'].startswith(prompt):
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
    else:

        for ele in launches:

            if ele['launch_service_provider']['name'] == prompt:
                
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

    newyears = sorted(newyears)

    fill_in_numbers(newyears)

    for i in range(len(newyears)):

        newyears[i] = str(newyears[i])

    for ele in newyears:
        if ele not in years:
            years[ele] = [0, 0, 0, 0]

    years = dict(sorted(years.items()))

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

    plt.rcParams['font.size'] = '9'

    labelsbar = list(years.keys())
    for i in range(len(labelsbar)):
        labelsbar[i] = int(labelsbar[i])



    fig1 = plt.figure(figsize=(10, 3))
    plot2 = fig1.add_subplot(111)



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

    plt.title("Launches per year: " + prompt + " rockets")

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




    maxvalue = 0
    for ele in years:
        current = years[ele][3]

        if current > maxvalue:
            maxvalue = current
    if maxvalue < 10:
        plot2.yaxis.set_ticks(np.arange(start, end+1, 1))

    plot2.legend(bbox_to_anchor=(1,1), loc="upper left", fontsize=8)
    plt.ylim(top=maxvalue+1)
    filename = str("agency"+"_" + prompt)
    filename = filename.replace("/", "_")
    plt.savefig("Graphs/"+filename + ".png", dpi=600)
    
    plt.show()




file2 = open("families.json")
rocket_families = json.load(file2)

file3 = open("names.json")
rocket_names = json.load(file3)

file4 = open("fullnames.json")
rocket_fullnames = json.load(file4)

file5 = open("agencies.json")
agencies = json.load(file5)


generate_graph("name", "Falcon 9")