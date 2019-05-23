# -*- coding: utf-8 -*-
"""
Download all articles of someone's Wechat blog
"""

# TODO: Go to the blog history webpage
#       Every page has n article links
# TODO: Get the article link, find the link url then download it
# TODO: Repeat it until download all the articles in one page
# TODO: Go to next page and repeat it until all articles have been
#       Downloaded.

import os
import sys
import requests
import bs4
import string
import re

url = 'https://chuansongme.com/account/chinaetfs'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0)'}
dir_name = 'etf_blog'
os.makedirs(dir_name, exist_ok=True)

def pg_soup(url):
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features='lxml')
    return (res, soup)

# Get last page url end strings to end
def find_pg_num(soup):
    pg_link_elems = soup.select('.w4_5 a')
    pg_num = pg_link_elems[len(pg_link_elems)-2].getText()
    pg_num = int(pg_num)
    return pg_num

def remove_invalid(value):
    for ch in string.punctuation:
        value = value.replace(ch, '')
    value = re.sub("(?<![ -~]) (?![ -~])", "", value)
    value = value.replace(' ', '')
    return value

n = 1
res, soup = pg_soup(url)
pg_num = find_pg_num(soup)
# print(pg_num)

while n <= pg_num:
    print('Downloading atrticles from page %s ...' % (url))
    res, soup = pg_soup(url)
    atc_link_elems = soup.select('.question_link')
    # print(atc_link_elems)
    num_link = len(atc_link_elems)
    # print(num_link)

    if atc_link_elems == []:
        print('Could not find the page.')
    else:
        for i in range(num_link):
            # Get each articl url
            atc_url = atc_link_elems[i].get('href')
            atc_url = 'https://chuansongme.com' + atc_url
            print('Downloading from %s ...' % (atc_url))
            # Go to the single atc page
            act_res, act_soup = pg_soup(atc_url)

            act_title = act_soup.select('.rich_media_title')[0].getText()
            act_title = remove_invalid(act_title)

            act_time = act_soup.select('.rich_media_meta_list em')[0].getText()

            saved_title = act_time + '-' + act_title
            print('Downloaded: %s...' % (saved_title))

            act_html = open(os.path.join(dir_name, saved_title + '.html'), 'wb')
            for chunk in act_res.iter_content(100000):
                act_html.write(chunk)

            act_html.close()

    if n < pg_num:
        pg_link_elems = soup.select('.w4_5 a')
        next_pg_url = pg_link_elems[len(pg_link_elems)-1].get('href')
        url = 'https://chuansongme.com' + next_pg_url
    
    n += 1
