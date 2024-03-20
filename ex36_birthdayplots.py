import json
from collections import Counter
from bokeh.plotting import figure, show, output_file

output_file("plot.html")
with open("famous_scientist_birthdays.json","r") as f:
    scientist_list = json.load(f)

month_numbers = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

months = []

for name, birthday in scientist_list.items():
    month = int(birthday.split("-")[1])
    months.append(month_numbers[month])
months = Counter(months)

months, counts = list(zip(*months.items()))

categories = list(month_numbers.values())
p = figure(x_range = categories, title = "Scientist Birthday Months")
p.xaxis.major_label_orientation = "vertical"
p.scatter(months, counts, size = 10)
show(p)