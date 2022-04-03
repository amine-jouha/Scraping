import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json
import csv
filecsv = open('managa.csv', 'w', encoding='utf8')
# Set the URL you want to webscrape from
file = open('manga.json', 'w', encoding='utf8')
file.write('[\n')
data = {}
csv_columns = [ 'chapter','img', 'name']
page=319
for page in range(1000,1002):
    # for p in range(1,17):
        print('---', page, '---')
        url = 'https://one-piecescan.com/manga/one-piece-scan-'+str(page)+'/'#+str(p)
        print(url)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        ancher = soup.find_all(
            'img',{'border':'0'})
        writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
        i = 0
        #print(ancher)
        for i in ancher:
          writer.writeheader()
          name = i.find('img')
          writer.writerow({'chapter':str(page),'img': " ".join(i.get('src').split())})
          data['chapter']=str(page)
          data['img'] = " ".join(i.get('src').split())
          json_data = json.dumps(data, ensure_ascii=False)
          file.write(json_data)
          file.write(",\n")
file.write("\n]")
filecsv.close()
file.close()



# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# import requests
# driver = webdriver.Chrome(ChromeDriverManager().install())
# #driver = webdriver.Chrome("C:/chromedriver.exe")
# driver.maximize_window()
# file1 = open("Myimages.txt","a") 
# wait = WebDriverWait(driver, 3)
# import urllib.request
# for l in range(115,120):
#     for i in range(1,17):
#         driver.get("https://www.scan-vf.net/one_piece/chapitre-"+str(l)+"/"+str(i))
#         img_tags = driver.find_elements_by_tag_name('img')
#         imags = []
#         print(len(img_tags))
#         for img in img_tags:
#             imags.append(img.get_attribute('src'))
#             print(img.get_attribute('src'))
#             f = open(img.get_attribute('alt')+'.jpg','wb')
#             f.write(requests.get(img.get_attribute('src')).content)
#             f.close()






# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager
# import requests
# driver = webdriver.Chrome(ChromeDriverManager().install())
# for c in range (100,102):
#     for i in range (1,40):
#         driver.get("https://www.scan-vf.net/one_piece/chapitre-"+str(c)+"/"+str(i))
#         elem = driver.find_elements_by_tag_name("img")
#         print(elem)
#         for img in elem:
#             f = open(img.get_attribute('alt')+'.jpg','wb')
#             f.write(requests.get(img.get_attribute('src')).content)
#             f.close()
#             print(img.get_attribute("src"))
# driver.close()




