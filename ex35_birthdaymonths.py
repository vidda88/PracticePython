import json
from collections import Counter

with open("famous_scientist_birthdays.json","r") as f:
    scientist_list = json.load(f)

months = []
for value in scientist_list:
    temp = scientist_list[value]
    if temp[5:7] == '01':
        months.append('January')
    if temp[5:7] == '02':
        months.append('February')
    if temp[5:7] == '03':
        months.append('March')
    if temp[5:7] == '04':
        months.append('April')
    if temp[5:7] == '05':
        months.append('May')
    if temp[5:7] == '06':
        months.append('June')
    if temp[5:7] == '07':
        months.append('July')
    if temp[5:7] == '08':
        months.append('August')
    if temp[5:7] == '09':
        months.append('September')
    if temp[5:7] == '10':
        months.append('October')
    if temp[5:7] == '11':
        months.append('November')
    if temp[5:7] == '12':
        months.append('December')

tally = Counter(months)
print("BIRTHDAY MONTHS")
print("January: {}".format(tally["January"]))
print("February: {}".format(tally["February"]))
print("March: {}".format(tally["March"]))
print("April: {}".format(tally["April"]))
print("May: {}".format(tally["May"]))
print("June: {}".format(tally["June"]))
print("July: {}".format(tally["July"]))
print("August: {}".format(tally["August"]))
print("September: {}".format(tally["September"]))
print("October: {}".format(tally["October"]))
print("November: {}".format(tally["November"]))
print("December: {}".format(tally["December"]))