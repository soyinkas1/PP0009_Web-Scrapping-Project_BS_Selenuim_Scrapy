
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

web = 'https://www.audible.co.uk/adblbestsellers?ref=a_search_t1_navTop_pl0cg1c0r0&pf_rd_p=f85ca050-5a0a-4b61-ad05-22714c60f1e2&pf_rd_r=4A6H4WYXC7VFER9ZXMW8&pageLoadId=33fbVEtbdOW68z63&creativeId=209a9396-a0bd-443c-93ab-d608f0c4ed36'
path = "C:\\Users\\USER\\OneDrive\\Documents\\PERSONAL\\PERSONAL DEVELOPMENT\\DATA SCIENCE\\Web_Scraping_Tutorial\\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service,options=options)
driver.get(web)
driver.maximize_window()

#pagination
pagination=driver.find_element(By.XPATH,'.//ul[contains(@class, "pagingElements")]')
pages = pagination.find_elements(By.TAG_NAME, 'li')
last_page = int(pages[-2].text)

current_page = 1
title = []
author = []
lenght = []
while current_page <= last_page:
    time.sleep(4)
    container =driver.find_element(By.CLASS_NAME, 'adbl-impression-container ')
    products = container.find_elements(By.XPATH, './/li[contains(@class, "productListItem")]')



    for product in products:
        title.append(product.find_element(By.XPATH, './/h3[contains(@class,"bc-heading")]').text)
        author.append(product.find_element(By.XPATH, './/li[contains(@class,"authorLabel")]').text)
        lenght.append(product.find_element(By.XPATH, './/li[contains(@class,"runtimeLabel")]').text)
    current_page =+ 1

    try:
        next_page = driver.find_element(By.XPATH, '//span[contains(@class, "nextButton")]')
        next_page.click()

    except:
        pass

driver.quit()

certificates
df =pd.DataFrame({'Title':title, 'Author': author, 'Lenght':lenght})
df.to_csv('page1_audible.csv',index=False)