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

driver = webdriver.Chrome()

headers = requests.utils.default_headers()
headers.update({
'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
})

def get_user_page(base_url):
    response = requests.get(base_url, headers=headers)
    content = BeautifulSoup(response.content, "html.parser")
    return content

def get_follower_page(base_url):
    #followers list is in <div class="css-1dbjc4n">...</div>
    url = base_url + "/following"
    response = requests.get(url, headers=headers)
    content = BeautifulSoup(response.content, "html.parser")
    return content

def main():
    modi_base_url = "https://twitter.com/narendramodi"
    html = get_follower_page(modi_base_url)

    print(html)

if __name__ == '__main__':
    main()
