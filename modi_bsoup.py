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

class Twitterbot:
    def __init__(self, login_times = 1):
        chrome_options = Options()
        self.driver = webdriver.Chrome(
            executable_path = os.path.join(os.getcwd(), 'chromedriver'),
            options = chrome_options)
        self.login_times = login_times
        self.control_login()

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

        friends_list = remove_duplicates(friends_list)
        self.write_to_csv(self.username, friends_list)

        return friends_list

    def remove_duplicates(self, list):
        already_seen = []
        for name in list:
            if name not in already_seen:
                already_seen.append(name)
        return already_seen

    def write_to_csv(self, username, friends_list):
        with open('usernames.csv', 'a+', newline='') as file:
            for name in friends_list:
                writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([username, name])
        file.close()

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
    bot = Twitterbot(login_times = 2)
    modi_friends = get_modi_friends_list()
    section_friends = get_friend_list_section(modi_friends, 0)
    print(section_friends)
    make_user_list(section_friends, bot)
    for user in section_friends:
        user.get_friends()
    bot.close()

if __name__ == '__main__':
    main()
