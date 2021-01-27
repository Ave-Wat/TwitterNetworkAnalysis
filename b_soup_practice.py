"""
python3 -m venv 'name'-env
'environment name'\Scripts\activate.bat
pip install bs4
pip install requests
pip install selenium
download appropriate driver: https://selenium-python.readthedocs.io/installation.html
"""

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
import time, os
import tokens

headers = requests.utils.default_headers()
headers.update({
'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
})

base_url = "https://twitter.com/"

class Twitterbot :
    def __init__(self):
        '''
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        options.add_argument('--headless')
        options.add_argument('--enable-javascript')
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36")
        '''
        chrome_options = Options()

        self.driver = webdriver.Chrome(
            executable_path = os.path.join(os.getcwd(), 'chromedriver'),
            options = chrome_options)

    def login(self):
        self.driver.implicitly_wait(25)
        self.driver.get("https://twitter.com/login")
        time.sleep(3)
        username = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        username.send_keys(tokens.ave_m)
        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        password.send_keys(tokens.ave_pass)
        time.sleep(2)

    def infinite_scroll(self, timeout):
        '''questionable'''
        scroll_pause_time = timeout
        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause_time)
            # Calculate new scroll height and compare with last scroll height
            new_height =self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                # If heights are the same it will exit the function
                break
            last_height = new_height

    def get_page(self, url):
        self.driver.implicitly_wait(30)
        self.driver.get(url)
        #self.bot.infinite_scroll(driver, 5)
        page_source = self.driver.page_source

        return page_source

class User:
    def __init__(self, username, bot):
        self.username = username
        self.bot = bot

    def get_user_page(self):
        url = base_url + self.username
        page_source = self.bot.get_page(url)
        content = BeautifulSoup(page_source, "html.parser")
        return content

    def get_followers(self):
        url = base_url + self.username + "/following"
        page_source = self.bot.get_page(url)
        content = BeautifulSoup(page_source, "html.parser")
        #followers list is in <div class="css-1dbjc4n">...</div>
        return content

def main():
    bot = Twitterbot()
    bot.login()
    modi = User("narendramodi", bot)
    html = modi.get_followers()

    print(html)

if __name__ == '__main__':
    main()
