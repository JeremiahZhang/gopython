#! /usr/bin/python3
# -*- coding: utf-8 -*-
# luck.py -- Opens several Google search results.
# reference: http://automatetheboringstuff.com/chapter11/

import sys
import webbrowser
import requests
import bs4

def googling():
    print('Googling ...')

    if len(sys.argv[1:]) > 0:
        search_item = ' '.join(sys.argv[1:])
        address = 'https://www.google.com/search?q=' + search_item
        # webbrowser.open(address)
        res = requests.get(address)
        res.raise_for_status()

        # TODO: Retrive top search result links
        soup = bs4.BeautifulSoup(res.text)

        link_elems = soup.select('.r a')
        # TODO: Open a browser tab for each result
        num_open = min(5, len(link_elems))
        for i in xrange(num_open):
            webbrowser.open('http://google.com' + link_elems[i].get('href'))
    else:
        address = 'https://www.google.com/'
        webbrowser.open(address)

# Cannot go to Google page in terminal just try Baidu Search
def baidu():
    print('Searching ...')
    
    if len(sys.argv[1:]) > 0:
        search_item = ' '.join(sys.argv[1:])
        addr = 'https://www.baidu.com/s?wd=' + search_item
        
        res = requests.get(addr)
        res.raise_for_status()
        
        soup = bs4.BeautifulSoup(res.text)
        link_elems = soup.select('.t a')
        
        num_open = min(3, len(link_elems))
        for i in range(num_open):
            webbrowser.open(link_elems[i].get('href'))

def sogou():
    print('Using sogou searching')
    
    if len(sys.argv[1:]) > 0:
        search_item = ' '.join(sys.argv[1:])
        url = 'https://www.sogou.com/web?query=' + search_item
        
        res = requests.get(url)
        res.raise_for_status()
        
        soup = bs4.BeautifulSoup(res.text)
        link_elems = soup.select('.result .pt a')
        num_open = len(link_elems)
        for i in range(num_open):
            webbrowser.open(link_elems[i].get('href'))

if __name__ == '__main__':
    googling()
    # baidu()
    # sogou()

# warnning 
"""
.\web-crawler> python lucky.py python
Using sogou searching
D:\ProgramData\Anaconda2\envs\ten_years\lib\site-packages\bs4\__init__.py:181: 
UserWarning: No parser was explicitly specified, so I'm using the best
available HTML parser for this system ("lxml"). 
This usually isn't a problem, but if you run this code on another system, 
or in a different virtual environment, 
it may use a different parser and behave differently.

The code that caused this warning is on line 70 of the file lucky.py. 
To get rid of this warning, change code that looks like this:

 BeautifulSoup(YOUR_MARKUP})

to this:

 BeautifulSoup(YOUR_MARKUP, "lxml")

  markup_type=markup_type))
"""