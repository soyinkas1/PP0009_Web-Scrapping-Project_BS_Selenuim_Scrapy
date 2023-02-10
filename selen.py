from selenium import webdriver

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = 'C:\\Users\\USER\\OneDrive\\Documents\\PERSONAL\\PERSONAL\ DEVELOPMENT\\DATA SCIENCE\\Web_Scraping_Tutorial\\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(website)

