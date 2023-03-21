from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Import the file with the twitter accounts




web = "https://twitter.com/search?q=startup%2Bwomen&src=typed_query"
path = "C:\\Users\\USER\\OneDrive\\Documents\\PERSONAL\\PERSONAL DEVELOPMENT\\DATA SCIENCE\\Web_Scraping_Tutorial\\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(web)
driver.maximize_window()
# time.sleep(8)



def get_tweets(element):
    global views_data
    try:
        user = element.find_element(By.XPATH, './/span[contains(text(),"@")]').text
        text = element.find_element(By.XPATH, './/div[@lang]').text
        stats = element.find_elements(By.XPATH, './/span[@data-testid]')
        comments_data = stats[0].text
        retweets_data = stats[1].text
        likes_data = stats[2].text
        views_data = stats[3].text
    except:
        tweet_data = ['user', 'text', 'comments', 'retweet', 'likes', 'views']

    tweet_data = [user, text, comments_data, retweets_data, likes_data, views_data]

    return tweet_data


user_data = []
texts = []
comment_data = []
retweet_data = []
like_data = []
view_data = []
tweet_ids = set()

scrolling = True
while scrolling:
    tweets = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, "//article[@role='article']")))
    for tweet in tweets[-15:]:
        tweet_data = get_tweets(tweet)
        tweet_id = ''.join(tweet_data)
        if tweet_id not in tweet_ids:
            tweet_ids.add(tweet_id)
            user_data.append(tweet_data[0])
            texts.append(" ".join(tweet_data[1].split()))
            comment_data.append(tweet_data[2])
            retweet_data.append(tweet_data[3])
            like_data.append(tweet_data[4])
            view_data.append(tweet_data[5])
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        # if new_height == last_height:
        #     scrolling = False
        #     break
        if new_height == last_height or len(user_data) > 100:
            scrolling = False
            break
        else:
            last_height = new_height
            break







driver.quit()

tweet_df = pd.DataFrame({'user': user_data, 'text': texts, 'comments': comment_data, 'retweets': retweet_data, 'likes': like_data, 'views': view_data})
tweet_df.to_csv('company_.csv', index=False)
print(tweet_df)