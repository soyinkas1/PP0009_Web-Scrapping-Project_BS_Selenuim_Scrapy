import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time




web = "https://twitter.com/i/flow/login"
path = "C:\\Users\\USER\\OneDrive\\Documents\\PERSONAL\\PERSONAL DEVELOPMENT\\DATA SCIENCE\\Web_Scraping_Tutorial\\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service,options=options)
driver.get(web)
driver.maximize_window()

# wait of 6 seconds to let the page load the content
time.sleep(6)  # this time might vary depending on your computer

# locating username and password inputs and sending text to the inputs
# username
username = driver.find_element(By.XPATH,'//input[@autocomplete ="username"]')
username.send_keys("engrsho@yahoo.com")  # Write Email Here
# username.send_keys(os.environ.get("TWITTER_USER"))

# Clicking on "Next" button
next_button = driver.find_element(By.XPATH, '//div[@role="button"]//span[text()="Next"]')
next_button.click()

# wait of 2 seconds after clicking button
time.sleep(2)

# password
password = driver.find_element(By.XPATH, '//input[@autocomplete ="current-password"]')
password.send_keys("Modupe1$")  # Write Password Here
# password.send_keys(os.environ.get("TWITTER_PASS"))

# locating login button and then clicking on it
login_button = driver.find_element(By.XPATH, '//div[@role="button"]//span[text()="Log in"]')
login_button.click()

# closing driver
driver.quit()
