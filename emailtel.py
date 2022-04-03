from bs4 import BeautifulSoup
import re
import requests

allsite = ["https://www.myway.ma/", "https://www.ibba.org/find-a-business-broker/"]
emails = []
tels = []
for l in allsite:
    r = requests.get(l)
    soup = BeautifulSoup(r.content, "html.parser")
    for link in soup.findAll('a', attrs={'href': re.compile("^mailto:"or"^mail"or"^email")}):
        emails.append(link.get('href'))
    for tel in soup.findAll('a', attrs={'href': re.compile("^tel:")}):
        tels.append(tel.get('href'))
print(emails)
print(tels)