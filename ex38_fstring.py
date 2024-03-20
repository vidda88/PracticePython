import datetime

name = str(input("What is your name? "))
age = int(input("What is your age? "))
print(f"Hi {name}. You will turn 100 in the year {datetime.datetime.now().year + (100-age)}.")