import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# website = 'https://subslikescript.com/movies_letter-A?page=3'
website = 'https://www.adamchoi.co.uk/overs/detailed'
path = "C:\\Users\\VG\\OneDrive\\Documents\\PERSONAL\\PERSONAL DEVELOPMENT\\DATA SCIENCE\\Web_Scraping_Tutorial\\chromedriver.exe"

#
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(executable_path=path)
driver = webdriver.Chrome(executable_path=path,options=options)
driver.get(website)

all_matches_button = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')

all_matches_button.click()

dropdown = Select(driver.find_element(By.ID,'country'))
dropdown.select_by_visible_text('Italy')

time.sleep(4)




matches = driver.find_elements(By.TAG_NAME,'tr')

# print(matches)

date = []
home_team = []
score = []
away_team =[]

for match in matches:
    date.append(match.find_element(By.XPATH, './td[1]').text)
    home = match.find_element(By.XPATH, './td[2]').text
    home_team.append(home)
    print(home)
    score.append(match.find_element(By.XPATH, './td[3]').text)
    away_team.append(match.find_element(By.XPATH, './td[4]').text)

df = pd.DataFrame({'date': date, 'home': home_team, 'score': score, 'away_team': away_team})
df.to_csv('football_scraped.csv',index=False)

driver.quit()
