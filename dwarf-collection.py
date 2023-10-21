from bs4 import BeautifulSoup
import time
import pandas
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

browser = webdriver.Chrome("")
browser.get(URL)

time.sleep(10)
scraped_data = []
dwarf_data = []

def scrape():
    soup = BeautifulSoup(browser.page_source,"html.parser")

    table = soup.find('table',attrs={"class","wikitable sortable jquery-tablesorter"})
    tbody = table.find('tbody')
    tr_tags = tbody.find_all('tr')

    for td_tag in tr_tags:
        td_tags = td_tag.find_all('td')
        temp_list = []
        for col_data in td_tags:
            data = col_data.text.strip()
            print(data)
            temp_list.append(data)
            scraped_data.append(temp_list)

    for index in range(0,len(scraped_data)):
        star_name = scraped_data[index][1]
        radius = scraped_data[index][10]
        mass = scraped_data[index][9]
        distance = scraped_data[index][6]
        required_data = [star_name,distance,mass,radius]
        dwarf_data.append(required_data)
scrape()
headers = ["star_name","radius","mass","distance"]
dwarf_df = pandas.DataFrame(dwarf_data,columns=headers)
dwarf_df.to_csv('new_scraped_data.csv',index = True, index_label="id")
