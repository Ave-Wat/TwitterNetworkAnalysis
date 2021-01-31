from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
import time, os
import tokens
import random

class Twitterbot:
    def __init__(self, bot_number, login_times = 1):
        chrome_options = Options()
        self.driver = webdriver.Chrome(
            executable_path = os.path.join(os.getcwd(), 'chromedriver'),
            options = chrome_options)
        self.login_times = login_times
        self.bot_number = bot_number
        self.control_login()

    def get_bot_number(self):
        return self.bot_number

    def control_login(self):
        if self.login_times == 1:
            self.login(tokens.ave_m, tokens.ave_pass)
        else:
            self.login(tokens.ave_m, tokens.ave_pass)
            self.login(tokens.ave_u, tokens.ave_pass)

    def close(self):
        self.driver.close()

    def login(self, field1, field2):
        self.driver.implicitly_wait(25)
        self.driver.get("https://twitter.com/login")
        time.sleep(3)
        username = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        username.send_keys(field1)
        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        password.send_keys(field2)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div').click()
        time.sleep(3)

    def infinite_scroll_scrape(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        html = ""

        while True:
            html = html + self.driver.page_source

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

        self.hard_reload()

        return html

    def hard_reload(self):
        self.driver.execute_script("location.reload(true);")
        time.sleep(5)

    def get_friends_html(self, url):
        self.driver.implicitly_wait(30)
        self.driver.get(url)
        time.sleep(5)
        html = self.infinite_scroll_scrape()
        return html

    def get_page(self, url):
        self.driver.implicitly_wait(30)
        self.driver.get(url)
        return self.driver.page_source
