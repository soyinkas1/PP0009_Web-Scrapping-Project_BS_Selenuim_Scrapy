
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

web = 'https://www.audible.co.uk/search'
path = "C:\\Users\\USER\\OneDrive\\Documents\\PERSONAL\\PERSONAL DEVELOPMENT\\DATA SCIENCE\\Web_Scraping_Tutorial\\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.headless = True
options.add_argument('window-size=1920x1080')
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service,options=options)
driver.get(web)
# driver.maximize_window()

container =driver.find_element(By.CLASS_NAME, 'adbl-impression-container ')
products = container.find_elements(By.XPATH, './/li[contains(@class, "productListItem")]')

title = []
author = []
lenght = []

for product in products:
    title.append(product.find_element(By.XPATH, './/h3[contains(@class,"bc-heading")]').text)
    author.append(product.find_element(By.XPATH, './/li[contains(@class,"authorLabel")]').text)
    lenght.append(product.find_element(By.XPATH, './/li[contains(@class,"runtimeLabel")]').text)
print(title)
driver.quit()


df =pd.DataFrame({'Title':title, 'Author': author, 'Lenght':lenght})
df.to_csv('page1_audible_nohead.csv',index=False)