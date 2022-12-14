import os
import json
import csv
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
URLcantonagain = 'https://www.thebankofcanton.com/rates/'
URLstoughton = 'https://www.stoughtoncoop.bank/resources/rates-calculators/mortgage-rate/'

abington = "bankofabington.txt"
easton = "bankofeaston.txt"
canton = "bankofcanton.txt"
sharon = "bankofsharon.txt"
cantonagain = "bankofcantonagain.txt"
stoughton = "bankofstoughton.txt"

tableAbington = dict()
tableEaston = []
tableCanton = []
tableSharon = []
tableSouthShore = []
tableCantonAgain = [] 
tableStoughton = []

def printTable(table, tablename):
    for k in table:
        print(tablename, ":")
        print(k)
        print("----------------")

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


# Use selnium to grab web page
def getWebPage(url):
    # South shore website uses json, so we'll make an exception
    if(url == URLsouthshore):
        return get_web_json(url)
    options = Options()
    options.add_argument('--headless')
    options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    time.sleep(4)
    r = driver.page_source
    return r
# Get JSON data, only used for south shore
def get_web_json(url):
   request = requests.get(url)
   text = request.text 
   return json.loads(text)
# Check if the file exists, if not, make a new file with data from URL
def makeFile(filename, url):
    if (os.path.exists(filename)):
        print("File ", filename, " exists.. Skipping")
    elif (not(os.path.exists(filename))):
        print("Data does not exist for ", filename, "please wait while website is retrieved.")
        filename = os.path.join(path, filename)
        f = open(filename, 'w', encoding="utf-8")
        data = getWebPage(url)
        f.write(str(data))
        f.close()
        print("Data collection done for ", filename)
# Read file, simple.
def readFile(filename):
    with open(filename, 'r', errors='ignore') as file:
        return file.read()

def writetoCSV(table):
    filename = 'out.csv'
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("File does not exist.")
    with open(filename, 'w', newline='') as resultFile:
        fieldnames = []
        values = []
        output = csv.writer(resultFile, dialect = 'excel')
        for k,v in table.items():
            fieldnames = []
            fieldnames.append([k])
        output.writerows(fieldnames)
        for k,v in table.items():
            values = []
            values.append([v])
            print(values)
        output.writerows(values)

# ----------------------------- Below are specific data extracting functions for each website, subject to change.
def abingtonData(filename):
    soup = BeautifulSoup(str(readFile(filename)), 'html.parser')
    # 30 year mortage fixed 0 points 
    thirtyYearMortage = soup.table.find_all('tr')[2].find_all('td')[1]
    # 20 year mortage fixed 0 points 
    twentyYearMortage = soup.table.find_all('tr')[4].find_all('td')[1]
    # 15 year mortage fixed 0 points
    fifteenYearMortage = soup.table.find_all('tr')[6].find_all('td')[1]
    # 3/3 ARM 0 Pts 
    threeThreeArm = soup.find_all('table')[2].find_all('tr')[2].find_all('td')[1]
    # 5/5 ARM
    fiveFiveArm = soup.find_all('table')[2].find_all('tr')[3].find_all('td')[1]
    # 7/3 ARM 
    sevenThreeArm = soup.find_all('table')[2].find_all('tr')[1].find_all('td')[1]

    tableAbington['30 year mortage'] = remove_tags(thirtyYearMortage)
    tableAbington['20 year mortage'] = remove_tags(twentyYearMortage)
    tableAbington['15 year mortage'] = remove_tags(fifteenYearMortage)
    tableAbington['3/3 ARM'] = remove_tags(threeThreeArm)
    tableAbington['5/5 ARM'] = remove_tags(fiveFiveArm)
    tableAbington['7/3 ARM'] = remove_tags(sevenThreeArm)

    
def eastonData(filename):
    soup = BeautifulSoup(str(readFile(filename)), 'html.parser')
    # 30 year mortage fixed 0 points 
    thirtyYearMortage = soup.find_all('table')[1].find_all('tr')[4].find_all('td')[1]
    # 20 year mortage fixed 0 points
    twentyYearMortage = soup.find_all('table')[1].find_all('tr')[3].find_all('td')[1]
    # 15 year mortage fixed 0 points
    fifteenYearMortage = soup.find_all('table')[1].find_all('tr')[2].find_all('td')[1]
    # 10 year mortage fixed 0 points
    tenYearMortage = soup.find_all('table')[1].find_all('tr')[1].find_all('td')[1]
    #5/1 ARM
    fiveOneArm = soup.find_all('table')[3].find_all('tr')[1].find_all('td')[1]
    #7/1 ARM
    SevenOneArm = soup.find_all('table')[3].find_all('tr')[2].find_all('td')[1]
    tableEaston.append([remove_tags(thirtyYearMortage), remove_tags(twentyYearMortage), remove_tags(fifteenYearMortage), remove_tags(tenYearMortage), remove_tags(fiveOneArm), remove_tags(SevenOneArm)])

    
def cantonData(filename):
    soup = BeautifulSoup(str(readFile(filename)), 'html.parser')
    # 30 year mortage fixed 0 points 
    thirtyYearMortage = soup.find_all('table')[0].find_all('tr')[3].find_all('td')[0]
    # 15 year mortage fixed 0 points
    fifteenYearMortage = soup.find_all('table')[0].find_all('tr')[6].find_all('td')[0]
    #5/1 ARM 
    fiveOneArm = soup.find_all('table')[0].find_all('tr')[9].find_all('td')[0]
    tableCanton.append([remove_tags(thirtyYearMortage), remove_tags(fifteenYearMortage), remove_tags(fiveOneArm)])


def sharonData(filename):
    soup = BeautifulSoup(readFile(filename), 'html.parser')
    # 30 year mortage 0 points 
    thirtyYearMortage = soup.find_all(class_='content_rates_table')[0].find_all('tr')[9].find_all('td')[1]
    # 20 year mortage 0 points 
    twentyYearMortage = soup.find_all(class_='content_rates_table')[0].find_all('tr')[7].find_all('td')[1]
    # 15 year mortage 0 points 
    fifteenYearMortage = soup.find_all(class_='content_rates_table')[0].find_all('tr')[5].find_all('td')[1]
    #3/1 ARM 0 points 
    threeOneArm = soup.find_all(class_='content_rates_table')[3].find_all('tr')[5].find_all('td')[1]
    #5/1 ARM 0 points 
    fiveOneArm = soup.find_all(class_='content_rates_table')[3].find_all('tr')[7].find_all('td')[1]
    #7/1 ARM 0 points 
    sevenOneArm = soup.find_all(class_='content_rates_table')[3].find_all('tr')[9].find_all('td')[1]
    #10/1 ARM 0 points 
    tenOneArm = soup.find_all(class_='content_rates_table')[3].find_all('tr')[11].find_all('td')[1]
    #15/1 ARM 0 points 
    fifteenOneArm = soup.find_all(class_='content_rates_table')[3].find_all('tr')[13].find_all('td')[1]
    tableSharon.append([remove_tags(thirtyYearMortage), remove_tags(twentyYearMortage), remove_tags(fifteenYearMortage), remove_tags(threeOneArm), remove_tags(fiveOneArm), remove_tags(sevenOneArm), remove_tags(tenOneArm), remove_tags(fifteenOneArm)])


def southshoreData(url):
    data = getWebPage(url)
    # 30 year fixed 0 points
    thirtyYearMortage = data['$values'][0]['indicatorRate']
    # 20 year fixed 0 points
    twentyYearMortage = data['$values'][1]['indicatorRate']
    # 15 year fixed 0 points
    fifteenYearMortage = data['$values'][2]['indicatorRate']
    # 10 year fixed 0 points
    tenYearMortage = data['$values'][3]['indicatorRate']
    # 10/5 ARM 0 points 
    tenFiveArm = data['$values'][4]['indicatorRate']
    tableSouthShore.append([thirtyYearMortage, twentyYearMortage, fifteenYearMortage, tenYearMortage, tenFiveArm])

def cantonagainData(filename):
    soup = BeautifulSoup(readFile(filename), 'html.parser')
    # 30 year mortage fixed 0 points 
    thirtyYearMortage = soup.find_all('table')[4].find_all('tr')[1].find_all('td')[2]
   # 15 year mortage fixed 0 points
    fifteenYearMortage = soup.find_all('table')[4].find_all('tr')[3].find_all('td')[2]
    tableCantonAgain.append([remove_tags(thirtyYearMortage), remove_tags(fifteenYearMortage)])

def stoughtonData(filename):
    soup = BeautifulSoup(readFile(filename), 'html.parser')
     # 30 year mortage fixed 0 points 
    thirtyYearMortage = soup.find_all('table')[0].find_all('tr')[1].find_all('td')[2]
    # 20 year mortage fixed 0 points
    twentyYearMortage = soup.find_all('table')[0].find_all('tr')[4].find_all('td')[2]
    # 15 year mortage fixed 0 points
    fifteenYearMortage = soup.find_all('table')[0].find_all('tr')[7].find_all('td')[2]
    # 10 year mortage fixed 0 points
    tenYearMortage = soup.find_all('table')[0].find_all('tr')[10].find_all('td')[2]
    tableStoughton.append([remove_tags(thirtyYearMortage), remove_tags(twentyYearMortage), remove_tags(fifteenYearMortage), remove_tags(tenYearMortage)])






    


# ------- abington ------------
makeFile(abington, URLabington)
abingtonData(abington)
printTable(tableAbington, abington)
# ------- Easton ------------
makeFile(easton, URLeaston)
eastonData(easton)
printTable(tableEaston, easton)
# ------- Canton ------------
makeFile(canton, URLcanton)
cantonData(canton)
printTable(tableCanton, canton)
# ------- Sharon ------------
makeFile(sharon, URLsharon)
sharonData(sharon)
printTable(tableSharon, sharon)
# ------- South Shore ------------
# South shore is a special circumstance. Website is JSON, don't need to make a file.
southshoreData(URLsouthshore)
printTable(tableSouthShore, "South Shore")
# ------- Canton Again ------------
makeFile(cantonagain, URLcantonagain)
cantonagainData(cantonagain)
printTable(tableCantonAgain, "Canton, again.")
# ------- Stoughton ------------
makeFile(stoughton, URLstoughton)
stoughtonData(stoughton)
printTable(tableStoughton, " Stoughton: ")


#writetoCSV(tableAbington)


