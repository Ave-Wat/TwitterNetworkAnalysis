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
        for line in usernames_list:
            friends_list.append(line.get('href')[1:])

        friends_list = self.remove_duplicates(friends_list)
        self.write_to_csv(self.username, friends_list)

        return friends_list

    def remove_duplicates(self, list):
        already_seen = []
        for name in list:
            if name not in already_seen:
                already_seen.append(name)
        return already_seen

    def write_to_csv(self, username, friends_list):
        filename = 'data/usernames' + str(self.bot.get_bot_number()) + '.csv'
        with open(filename, 'a+', newline='') as file:
            for name in friends_list:
                writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([username, name])
        file.close()
