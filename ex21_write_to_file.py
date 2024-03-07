import requests
from bs4 import BeautifulSoup

url = 'https://mtnsolutions.pro'
r = requests.get(url)
mtn = BeautifulSoup(r.text,'html.parser')
articles = mtn.select('h3')

print("MTN Solutions Articles:")
with open('mtn_articles.txt','w') as open_file:
    for instance in articles:
        print("Article:",instance.text)
        open_file.write(str(instance.text + "\n"))
print("Finished!")