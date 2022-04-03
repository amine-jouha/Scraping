import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json
import csv
filecsv = open('SouqDataapple.csv', 'w',encoding='utf8')
file = open('SouqDataapple.json','w',encoding='utf8')
# Set the URL you want to webscrape from
url = 'https://www.jumia.ma/telephone-tablette/?page='
file.write('[\n')
data = {}
csv_columns = ['name','price','img']
for page in range(5):
    print('---', page, '---')
    r = requests.get(url + str(page))
    print(url + str(page))
    soup = BeautifulSoup(r.content, "html.parser")
    ancher=soup.find_all('article',{'class' : 'prd _fb col c-prd'})
    writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
    i=0
    writer.writeheader()
    for pt in ancher:
        name = pt.find('h3',{'class':'name'})
        price = pt.find('div',{'class':'prc'})
        img = pt.find('img',{'class':'img'})

        if img:      
            writer.writerow({'name': name.text.replace('                    ', '').strip('\r\n'), 'price': price.text, 'img': img.get('data-src')})
            data['name'] =name.text.replace('                    ', '').strip('\r\n')
            data['price'] =price.text
            data['img'] =img.get('data-src')
            json_data = json.dumps(data,ensure_ascii=False)
            file.write(json_data)
            file.write(",\n")
        

file.write("\n]")
filecsv.close()
file.close()
