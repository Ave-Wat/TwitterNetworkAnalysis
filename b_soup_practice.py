"""
python3 -m venv 'name'-env
'environment name'\Scripts\activate.bat
pip install bs4
pip install requests
"""

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
options.add_argument('--enable-javascript')

driver = webdriver.Chrome(options=options)

headers = requests.utils.default_headers()
headers.update({
'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
})

base_url = "https://twitter.com/"

def infinite_scroll(driver, timeout):
    scroll_pause_time = timeout
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            # If heights are the same it will exit the function
            break
        last_height = new_height

def get_user_page(username):
    url = base_url + username
    response = requests.get(url, headers=headers)
    content = BeautifulSoup(response.content, "html.parser")
    return content

def get_follower_page(username):
    url = base_url + username + "/following"
    driver.implicitly_wait(30)
    driver.get(url)
    #infinite_scroll(driver, 5)
    page_source = driver.page_source
    driver.close()

    content = BeautifulSoup(page_source, "html.parser")
    #followers list is in <div class="css-1dbjc4n">...</div>

    return content

def main():
    username = "narendramodi"
    html = get_follower_page(username)

    print(html)

if __name__ == '__main__':
    main()
