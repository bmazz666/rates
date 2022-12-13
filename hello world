import os
import json
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from bs4 import BeautifulSoup

path = 'P:\IT\Bmazzella\Coding'
os.chdir(path)

URLabington = 'https://abingtonbank.com/rates/mortgage-rates/'
URLeaston = 'https://www.bankofeaston.com/mortgage-rates/'
URLcanton = 'https://cantoncoopbank.mortgagewebcenter.com/'
URLsharon = 'https://www.scucu.com/personal/rates/mortgage-rates'
URLsouthshore = 'https://quickquote-consumer.optimalblue.com/api/featuredRates/indications/7d856416-fbc5-4385-80dd-3acf193ada60'

tableAbington = []
tableEaston = []
tableCanton = []
tableSharon = []
tableSouthShore = []

def remove_tags(html):
    html = str(html)
    start = (html.find('>'))
    end = (html.rfind('<'))
    start = start + 1
    cleaned = html[start:end]
    if((html.find('>') >= 1)):
        return(remove_tags(cleaned))
    else:
        return cleaned

    
    

"""  if(cleaned.find('>')):
        remove_tags(html)
    else: 
        return cleaned """

# Use selnium to grab web page
def getWebPage(url):
    options = Options()
    options.add_argument('--headless')
    options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    time.sleep(4)
    r = driver.page_source
    return r

def get_web_json(url):
   request = requests.get(url)
   text = request.text 
   return text

def makeFile(filename, data):
    if (os.path.exists(filename)):
        with open(filename, 'r') as f:
            content = f.read()
            return content 
    elif (not(os.path.exists(filename))):
        filename = os.path.join(path, filename)
        f = open(filename, 'w', encoding="utf-8")
        f.write(data)
        f.close()
        print("Data collection done")
        exit(1)
           
def openFile(filename, url):
    if (os.path.exists(filename)):
        with open(filename, 'r', encoding="utf-8") as f:
            content = f.read()
            return content
    elif (not(os.path.exists(filename))):
        print("File did not exist for ", filename, ". Retrieving website data, please wait for data. Rerun the program when done.")
        makeFile(filename, getWebPage(url))

def bankofabington(url):
    filename = 'bankofabington.txt'
    content = openFile(filename, url)
    soup = BeautifulSoup(str(content), 'html.parser')
    # 30 year mortage fixed 0 points 
    results = soup.table.find_all('tr')[2].find_all('td')[1]
    # 20 year mortage fixed 0 points 
    results2 = soup.table.find_all('tr')[4].find_all('td')[1]
    # 15 year mortage fixed 0 points
    results3 = soup.table.find_all('tr')[6].find_all('td')[1]
    # 3yr ARM 0 Pts 
    results4 = soup.find_all('table')[2].find_all('tr')[2].find_all('td')[1]
    # 5/5 ARM
    results5 = soup.find_all('table')[2].find_all('tr')[3].find_all('td')[1]
    tableAbington.append([remove_tags(results), remove_tags(results2), remove_tags(results3), remove_tags(results4), remove_tags(results5)])
    for k in tableAbington:
        print(k)
    
def bankofeaston(url):
    filename = 'bankofeaston.txt'
    content = openFile(filename, url)
    soup = BeautifulSoup(str(content), 'html.parser')
    # 30 year mortage fixed 0 points 
    results = soup.find_all('table')[1].find_all('tr')[4].find_all('td')[1]
    # 20 year mortage fixed 0 points
    results2 = soup.find_all('table')[1].find_all('tr')[3].find_all('td')[1]
    # 15 year mortage fixed 0 points
    results3 = soup.find_all('table')[1].find_all('tr')[2].find_all('td')[1]
    # 10 year mortage fixed 0 points
    results4 = soup.find_all('table')[1].find_all('tr')[1].find_all('td')[1]
    #5/1 ARM
    results5 = soup.find_all('table')[3].find_all('tr')[1].find_all('td')[1]
    #7/1 ARM
    results6 = soup.find_all('table')[3].find_all('tr')[2].find_all('td')[1]
    tableEaston.append([remove_tags(results), remove_tags(results2), remove_tags(results3), remove_tags(results4), remove_tags(results5), remove_tags(results6)])
    for k in tableEaston:
        print(k)
    
def bankofcanton(url):
    filename = 'bankofcanton.txt'
    content = openFile(filename, url)
    soup = BeautifulSoup(str(content), 'html.parser')
    # 30 year mortage fixed 0 points 
    results = soup.find_all('table')[0].find_all('tr')[3].find_all('td')[0]
    # 15 year mortage fixed 0 points
    results2 = soup.find_all('table')[0].find_all('tr')[6].find_all('td')[0]
    #5/1 ARM 
    results3 = soup.find_all('table')[0].find_all('tr')[9].find_all('td')[0]
    tableCanton.append([remove_tags(results), remove_tags(results2), remove_tags(results3)])
    for k in tableCanton:
        print(k)


def bankofsharon(url):
    filename = 'bankofsharon.txt'
    content = openFile(filename, url)
    soup = BeautifulSoup(str(content), 'html.parser')
    # 15 year mortage 0 points 
    results = soup.find_all(class_='content_rates_table')[0].find_all('tr')[5].find_all('td')[1]
    # 20 year mortage 0 points 
    results2 = soup.find_all(class_='content_rates_table')[0].find_all('tr')[7].find_all('td')[1]
    # 30 year mortage 0 points 
    results3 = soup.find_all(class_='content_rates_table')[0].find_all('tr')[9].find_all('td')[1]
    #3/1 ARM 0 points 
    results4 = soup.find_all(class_='content_rates_table')[3].find_all('tr')[5].find_all('td')[1]
    #5/1 ARM 0 points 
    results5 = soup.find_all(class_='content_rates_table')[3].find_all('tr')[7].find_all('td')[1]
    #7/1 ARM 0 points 
    results6 = soup.find_all(class_='content_rates_table')[3].find_all('tr')[9].find_all('td')[1]
    #10/1 ARM 0 points 
    results7 = soup.find_all(class_='content_rates_table')[3].find_all('tr')[11].find_all('td')[1]
    #15/1 ARM 0 points 
    results8 = soup.find_all(class_='content_rates_table')[3].find_all('tr')[13].find_all('td')[1]
    tableSharon.append([remove_tags(results), remove_tags(results2), remove_tags(results3), remove_tags(results4), remove_tags(results5), remove_tags(results6), remove_tags(results7), remove_tags(results8)])
    for k in tableSharon:
        print(k)
def bankofsouthshore(url):
    print(get_web_json(url))


    

bankofabington(URLabington)
bankofeaston(URLeaston)
bankofcanton(URLcanton)
bankofsharon(URLsharon)

#bankofsouthshore(URLsouthshore)
