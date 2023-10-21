from bs4 import BeautifulSoup
import time
import pandas
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("")
browser.get(URL)

time.sleep(10)
scraped_data = []
stars_data = []
def scrape():
    soup = BeautifulSoup(browser.page_source,"html.parser")
    startable = soup.find("table",attrs = {"class","wikitable sortable jquery-tablesorter"})
    tbody = startable.find('tbody')
    tr = tbody.find_all('tr')

    for row in tr:
        td = row.find_all('td')
        temp_list = []
        #print(td)

        for col_data in td:
            data = col_data.text.strip()
            #print(data)
            temp_list.append(data)
            scraped_data.append(temp_list)
    

    for i in range(0,len(scraped_data)):
        star_name = scraped_data[i][1]
        distance = scraped_data[i][3]
        mass = scraped_data[i][5]
        radius = scraped_data[i][6]
        lum = scraped_data[i][7]

        required_data = [star_name,distance,mass,radius,lum]
        stars_data.append(required_data)

scrape()
headers = ["star name","distance","mass","radius","luminosity"]
star_df = pandas.DataFrame(stars_data,columns=headers)
star_df.to_csv('scraped_data.csv',index = True, index_label="id")




