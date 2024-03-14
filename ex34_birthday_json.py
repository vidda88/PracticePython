import json
import requests
from bs4 import BeautifulSoup

info_json = {}
with open("famous_scientists.txt", "r") as f:
    names = f.readlines()
    for name in names:
        url = "https://en.wikipedia.org/wiki/{}".format(name.strip())
        r = requests.get(url)
        wiki = BeautifulSoup(r.text,'html.parser')
        bday = wiki.find("span", {"class": "bday"})
        info_json[name.replace("_"," ").strip()] = bday.get_text()
        print(name.replace("_"," ").strip(),bday.get_text())

with open("famous_scientist_birthdays.json","w") as f:
    json.dump(info_json,f)

print("Finished!")