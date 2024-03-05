import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture')
vfair = BeautifulSoup(r.text,'html.parser')
print(vfair.get_text())
