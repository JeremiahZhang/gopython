# -*- coding: utf-8 -*-
# Download every article from somesone's Sina Blog

# TODO: Download the page of history
# TODO: Get single article links,
#       every page has xx article links
# TODO: Find the url of the single article then download page
# TODO: Get the next button's url and repeat

import os
import sys
import requests
import bs4
import ftfy
import string
import re

def remove_invalid(value):
    for ch in string.punctuation:
        value = value.replace(ch, '')
    value = re.sub("(?<![ -~]) (?![ -~])", "", value)
    value = value.replace(' ', '')
    return value

# Article list page soup
def pg_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features='lxml')
    return soup

# Get the number of all pages
def pgs(soup):
    pgs_elems = soup.select('.SG_pages span')
    pg_num = pgs_elems[0].getText()
    pg_num = ftfy.fix_text(pg_num)
    pg_num = ''.join(x for x in pg_num if x.isdigit())
    total = int(pg_num) # Some blog have 239 pages
    return total

def main():
    url_num = input('Please enter the link of sina blog or enter 1.风中散发 2.养股 3.峰从海上来: ')
    if url_num == '1':
        url = 'http://blog.sina.com.cn/s/articlelist_1147298365_0_1.html'
        dir_name = 'fzsf_blog'
    elif url_num == '2':
        url = 'http://blog.sina.com.cn/s/articlelist_1664061535_0_1.html'
        dir_name = 'yang_blog'
    elif url_num == '3':
        url = 'http://blog.sina.com.cn/s/articlelist_2918184610_0_1.html'
        dir_name = 'feng_blog'
    else:
        url = url_num
        dir_name = input('Please enter the directory name to save the blog html files: ')

    pg_2_down = int(input('How many pages(0: all pages, 1: 1 pages): '))

    os.makedirs(dir_name, exist_ok=True)
    
    n = 1
    soup = pg_soup(url)
    if pg_2_down:
        end = pg_2_down
    else:
        end = pgs(soup)

    print(end)

    while n <= end:
        print('Downloading articles from %s ...' % (url))
        soup = pg_soup(url)
        atc_link_elems = soup.select('.atc_title a')
        num_link = len(atc_link_elems)

        if atc_link_elems == []:
            print('Could not find the page.')
        else:
            for i in range(num_link):
                # Get every single article url
                single_atc_url = atc_link_elems[i].get('href')
                print('Downloading the article from %s ...' % (single_atc_url))
                # Get to the single article page
                res = requests.get(single_atc_url)
                res.raise_for_status()
                # Get the html text
                act_soup = bs4.BeautifulSoup(res.text, features='lxml')
                # Get the article title name
                atc_time = act_soup.select('.time')[0].getText()
                atc_time = ''.join(e for e in atc_time if e.isalnum())
                print(atc_time)

                # Title name decode
                try:
                    tit_name = act_soup.select('.titName')[0].getText()
                    tit_name = ftfy.fix_encoding(tit_name)
                    tit_name = remove_invalid(tit_name)
                except IndexError:
                    tit_name = '转载'
                print(tit_name)
              
                try:  
                    html_file = open(os.path.join(dir_name, atc_time + '-' 
                                + tit_name + '.html'), 'wb')
                except OSError:
                    tit_name = remove_invalid(tit_name)
                    html_file = open(os.path.join(dir_name, atc_time + '-' 
                                + tit_name + '.html'), 'wb')

                for chunk in res.iter_content(100000):
                    html_file.write(chunk)

                html_file.close()

        # Next page element
        next_pg_elems = soup.select('.SG_pgnext a')
        # Next page link
        next_pg_link  = next_pg_elems[0].get('href')
        url = next_pg_link
        print(next_pg_link)

        print('Page %d has downloaded.' % (n))
        n += 1

    print('Done')

if __name__ == '__main__':
    main()
