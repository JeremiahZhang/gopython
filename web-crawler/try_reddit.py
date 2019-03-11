"""
source:
https://www.datacamp.com/community/tutorials/
    scraping-reddit-python-scrapy
"""

import requests
import csv
import time
from bs4 import BeautifulSoup

url = 'https://www.reddit.com/r/datascience/'
# url = 'http://xkcd.com'

# Headers to mimic a browser visit
headers = {'User-Agent': 'Mozilla/5.0'}

# Returns a requests.models.Response object
page = requests.get(url, headers=headers)
page.raise_for_status()

# Using BeautifulSoup to parse html
soup = BeautifulSoup(page.text, 'html.parser')

# Finding our tags
domains = soup.find_all('span', class_='domain')

# print('hello world')
# print(type(domains))

for domain in domains:
    if domain != '(self.datascience)':
        continue
    print('hello world')
    parent_div = domain.parent.parent.parent.parent
    print(parent_div.text)
    # print(domain.text)

# Finding our information
