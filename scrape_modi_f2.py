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
from twitterbot_class import Twitterbot
from user_class import User

headers = requests.utils.default_headers()
headers.update({'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",})

def get_modi_friends_list():
    modi_friends = []
    with open("modi_friends.csv", "rt", encoding="utf8") as file:
        mycsv = csv.reader(file)
        for row in mycsv:
            modi_friends.append(row[1])
    file.close()
    return modi_friends

def get_friend_list_section(friends_list, list_section_num, divide_list_by = 32):
    '''list_section_num is the section of list you want, from 0 to 1 less than divide_list_by'''

    section_len = len(friends_list)/divide_list_by
    slice_int_1 = int(section_len * list_section_num)
    slice_int_2 = int(section_len * (list_section_num + 1))
    return friends_list[slice_int_1:slice_int_2]

def make_user_list(list, bot):
    user_list = []
    for name in list:
        user_list.append(User(name, bot))
    return user_list

def main():
    bot = Twitterbot(1, login_times = 2)
    modi_friends = get_modi_friends_list()
    section_friends = get_friend_list_section(modi_friends, 0)
    print(section_friends)
    users = make_user_list(section_friends, bot)
    for user in users:
        user.get_friends()
    bot.close()

if __name__ == '__main__':
    main()
