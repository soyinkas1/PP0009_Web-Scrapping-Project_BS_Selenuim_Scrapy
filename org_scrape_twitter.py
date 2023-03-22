# Import the required libraries
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

# Set the path to the chrome webdriver
path = "C:\\Users\\VG\\OneDrive\\Documents\\PERSONAL\\PERSONAL DEVELOPMENT\\DATA SCIENCE\\Web_Scraping_Tutorial\\chromedriver.exe"

# Import the dataset containing the twitter accounts to scrape
social_df = pd.read_csv("C:\\Users\\VG\\OneDrive - Cardiff Metropolitan University\\Document Management\\Dissertation\\org_with_sm_500.csv")

# Create an empty dictionary to store tweets scraped
data = {}

# Helper function to scrape account details of the organisations
def get_follow():
    # global views_data
    try:
        following_data = driver.find_element(By.XPATH, '//a[contains(@href,"following")]//span/span').text
        follower_data = driver.find_element(By.XPATH, '//a[contains(@href,"followers")]//span/span').text

    except:
        follow_data = ['following_data', 'follower_data']

    follow_data = [follower_data, following_data]

    return follow_data

# Helper function to scrape each post
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


# search_box.send_Keys(Keys.ENTER)
# Scrape the twitter accounts in a loop
for twitter_page in social_df['twitter_url']:
    try:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        service = Service(executable_path=path)
        driver = webdriver.Chrome(executable_path=path, options=options)
        driver.get(twitter_page)
        driver.maximize_window()
        time.sleep(8)

        # Get details of the Twitter account
        following_data = []
        follower_data = []


        follow_data = get_follow()
        follower_data = follow_data[0]
        following_data = follow_data[1]

        # Refresh the page by searching for tweet mentions of the organisation
        name = twitter_page.split('/')
        name = name[-1]
        search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search Twitter']")
        search_box.send_keys(name, Keys.ENTER)
        time.sleep(8)
        # Create list to store the tweet details
        user_data = []
        texts = []
        comment_data = []
        retweet_data = []
        like_data = []
        view_data = []
        tweet_ids = set()

        # Scrape the tweets by scrolling infinitely
        scrolling = True
        while scrolling:
            tweets = WebDriverWait(driver, 8).until(EC.presence_of_all_elements_located((By.XPATH, "//article[@role='article']")))
            for tweet in tweets[-20:]:
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

                # Set maximum tweets
                if new_height == last_height or len(user_data) > 20:
                    scrolling = False
                    break
                else:
                    last_height = new_height
                    break
        # Add tweets details to a DataFrame
        tweet_df = pd.DataFrame(
            {'account': twitter_page, 'user': user_data, 'text': texts, 'comments': comment_data, 'retweets': retweet_data, 'likes': like_data,
             'views': view_data,'follower_data': follower_data, 'following_data': following_data})

        # Add the DataFrame to a dictionary
        data[f"{name}"] = tweet_df

        driver.quit()
    except:
        driver.quit()
        pass



# Save each DataFrame as a csv file for each entity
for key, val in data.items():
   val.to_csv("C:\\Users\\VG\\OneDrive - Cardiff Metropolitan University\\Document Management\\Dissertation\\Crunchbase Data\\tweets\\{}.csv".format(str(key)))
