import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# website = 'https://subslikescript.com/movies_letter-A?page=3'
website = 'https://www.fedcivilservice.gov.ng/mdas?d=1'
path = "C:\\Users\\VG\\OneDrive\\Documents\\PERSONAL\\PERSONAL DEVELOPMENT\\DATA SCIENCE\\Web_Scraping_Tutorial\\chromedriver.exe"

#
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(executable_path=path)
driver = webdriver.Chrome(executable_path=path, options=options)
driver.get(website)

# all_matches_button = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
#
# all_matches_button.click()
#
# dropdown = Select(driver.find_element(By.ID,'country'))
# dropdown.select_by_visible_text('Italy')
#
time.sleep(8)
#



mda_rows = driver.find_elements(By.TAG_NAME,'tr')
# print(mda_rows)
mda_code = []
org_min = []
mini_depart = []
agency_par = []
web = []

for mda in mda_rows:
    time.sleep(48)
    mda_code.append(mda.find_element(By.XPATH, './td[1]').text)
    org_min.append(mda.find_element(By.XPATH, './td[2]').text)
    # home_team.append(home)
    # print(home)
    mini_depart.append(mda.find_element(By.XPATH, './td[3]').text)
    agency_par.append(mda.find_element(By.XPATH, './td[4]').text)
    web.append(mda.find_element(By.XPATH, './td[5]').text)

df = pd.DataFrame({'MDA Code': mda_code, 'Organization/Ministries': org_min, 'Ministrarial Departments': mini_depart, 'Agencies/Parastals': agency_par,'Website': web})
df.to_csv('mda_data1.csv', index=False)

driver.quit()
