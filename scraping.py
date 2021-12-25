from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time

url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("D:/deepthi projects/C127/chromedriver.exe")
browser.get(url)

def scraping():
    headers=["magnitude","name","bayer_designation","distance","mass","radius","luminosity"]
    stars = []
    soup = BeautifulSoup(browser.page_source,"html.parser")
    all_tr_tags = soup.find_all("tr")
    for tr_tag in all_tr_tags:
        all_td_tags = tr_tag.find_all("tr")
        td_values = []
        for index,td_tag in enumerate(all_td_tags):
            if index==1:
                td_values.append(td_tag.find_all("a")[0].contents[0])
            else:
                td_values.append(td_tag.contents[0])
        stars.append(td_values)

    with open("scraped_data.csv","w") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(stars)

scraping()