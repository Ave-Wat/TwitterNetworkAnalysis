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
import random

headers = requests.utils.default_headers()
headers.update({'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",})

class Twitterbot :
    def __init__(self):
        chrome_options = Options()
        self.driver = webdriver.Chrome(
            executable_path = os.path.join(os.getcwd(), 'chromedriver'),
            options = chrome_options)
        self.login()
        self.login2()

    def close(self):
        self.driver.close()

    def login(self):
        self.driver.implicitly_wait(25)
        self.driver.get("https://twitter.com/login")
        time.sleep(3)
        username = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        username.send_keys(tokens.ave_m)
        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        password.send_keys(tokens.ave_pass)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div').click()
        time.sleep(3)

    def login2(self):
        self.driver.implicitly_wait(25)
        self.driver.get("https://twitter.com/login")
        time.sleep(3)
        username = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        username.send_keys(tokens.ave_u)
        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        password.send_keys(tokens.ave_pass)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div').click()
        time.sleep(3)

    def infinite_scroll_scrape(self):
        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        html = ""

        while True:
            html = html + self.driver.page_source

            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            scroll_pause_time = random.randint(4, 10)
            time.sleep(scroll_pause_time)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                # If heights are the same it will exit the function
                exit = input("Stop scrolling? (y/n): ")
                if exit == 'y':
                    break
                elif exit == 'n':
                    time.sleep(20)
                else:
                    time.sleep(10)
            last_height = new_height
        return html

    def get_friends_html(self, url):
        self.driver.implicitly_wait(30)
        self.driver.get(url)
        time.sleep(5)
        html = self.infinite_scroll_scrape()
        return html

class User:
    def __init__(self, username, bot):
        self.username = username
        self.bot = bot
        self.base_url = "https://twitter.com/"

    def get_user_page(self):
        url = self.base_url + self.username
        page_source = self.bot.get_page(url)
        content = BeautifulSoup(page_source, "html.parser")
        return content

    def get_friends(self):
        url = self.base_url + self.username + "/following"
        html = self.bot.get_friends_html(url)
        content = BeautifulSoup(html, "html.parser")
        usernames_list = content.find_all('a', {'class': 'css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21 r-1wbh5a2 r-dnmrzs r-1ny4l3l'}, href = True)

        friends_list = []
        friends_list.append(line.get('href')[1:])
        already_seen = []
        for name in friends_list:
            if name not in already_seen:
                already_seen.append(name)
        self.write_to_csv(self.username, already_seen)
        return already_seen

        def write_to_csv(username, friends_list):
            with open('usernames.csv', 'w', newline='') as file:
                for name in friends_list:
                    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([username, name])
            file.close()

def main():
    '''bot = Twitterbot()
    modi = User("narendramodi", bot)
    friends_list = modi.get_friends()
    bot.close()



if __name__ == '__main__':
    main()
