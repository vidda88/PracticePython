import requests
from bs4 import BeautifulSoup

url = 'https://nytimes.com'
r = requests.get(url)
mtn = BeautifulSoup(r.text,'html.parser')

selector = 'div.css-xdandi'

found = mtn.select(selector)

data = [x.text.split(';')[-1].strip() for x in found]

for x in data:
    print(x)
