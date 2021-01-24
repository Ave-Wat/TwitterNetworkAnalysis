"""
python3 -m venv 'name'-env
'name'-env\Scripts\activate.bat
pip install bs4
pip install requests
"""

from bs4 import BeautifulSoup
import requests
import csv

def get_content(url):
    headers = requests.utils.default_headers()
    headers.update({
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    })

    url = url
    response = requests.get(url, headers=headers)
    content = BeautifulSoup(response.content, "html.parser")
    return content

def main():
    html = get_content("https://twitter.com/narendramodi?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor")
    print(html)

if __name__ == '__main__':
    main()
