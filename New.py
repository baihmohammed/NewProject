#====================import the necessary libraries
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#================webdriver initialisa
export_path = "C:/Users/hp/PycharmProjects/pythonSeleniumBeautifulSoup"

#===================specify url and load the page_source after parse it to have the html code
url = "https://www.pretapartir.fr/recherche#!/search?th=SJ&depart=A_PAR&dureeNuit=7-99&sort=promo_desc"
driver.get(url)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1 strong")))
soup = BeautifulSoup(driver.page_source, "html.parser")

#====================Number of click that we should do to have the N_max of offers
Nb_Annonces = int(soup.find("h1").find("strong").get_text(strip=True))
nb_click = N_max/10 - 1 if Nb_Annonces >= N_max else Nb_Annonces/10

#=======================Use selenium to interact with the site by clicking buttons
for i in range(0, int(nb_click)):
    bt_next = driver.find_element(By.CSS_SELECTOR, "a[ng-click='vm.loadMorePackage()']")
    driver.execute_script("arguments[0].click()", bt_next)
    time.sleep(2)
    print(i)
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

#=======================list that contain all the <div/>
items = soup.find_all("div", {"class": "blocProduct-wrapper ng-scope"})
#=======================Function to clean the extracted data from spaces
def clean_text(str):
    return str.replace("\n", "").replace("\t", "").replace("   ", "")

#=======================Loop the item in the items list to extract necessary data
voyages = []
space = " "
for item in items:
    pays = clean_text(item.find("p", {"class": "blocProduct-place"}).get_text(strip=True))
    hotel = clean_text(item.find("p", {"class": "blocProduct-title"}).get_text(strip=True))
    details = item.find("div", {"class": "blocProduct-detail"}).findChildren()
    duree = clean_text(details[0].get_text(strip=True))
    depart = clean_text(details[1].get_text(strip=True))
    prix = item.find("div", {"class": "blocProduct-price"}).findChildren()[1].get_text(strip=1)
    voyage={
        "pays": pays,
        "hotel": hotel,
        "duree": duree,
        "depart": depart,
        "prix": prix,
    }
    voyages.append(voyage)
#================Use pandas to create dataframe and convert it to excel file that we can analyse after
import pandas as pd
df = pd.DataFrame(voyages)
print(df)

try:
     df.to_excel(export_path + "vaccances.xlsx", index=False)
     print("file created succefully!!")
     print(export_path)
except:
    print("can't create file!!")

