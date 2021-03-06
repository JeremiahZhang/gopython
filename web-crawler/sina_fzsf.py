# -*- coding: UTF-8 -*-
# Download every article from FZSF Sina Blog

# TODO: Download the page of history
# TODO: Get single article links,
#       every page has xx article links
# TODO: Find the url of the single article then download page
# TODO: Get the next button's url and repeat

import os
import requests
import bs4


url = 'http://blog.sina.com.cn/s/articlelist_1147298365_0_1.html' # blog history
os.makedirs('fzsf_sina_blog', exist_ok=True)
n = 0
end = 323  # all 323 页

while n < end:
    print('Downloading articles from %s ...' % (url))
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, features='lxml')
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
            # atc_titlename = act_soup.select('.titName')[0].getText()
            # atc_titlename = atc_titlename.encode() # string-utf8
            # atc_titlename = ''.join(e for e in atc_titlename if e.isalnum())
            # print(atc_titlename)
            atc_time = act_soup.select('.time')[0].getText()
            atc_time = ''.join(e for e in atc_time if e.isalnum())
            print(atc_time)
            html_file = open(os.path.join('fzsf_sina_blog', atc_time + '-' 
                            + os.path.basename(single_atc_url)), 'wb')
            for chunk in res.iter_content(100000):
                html_file.write(chunk)

            html_file.close()

    try:
        # Next page element
        next_pg_elems = soup.select('.SG_pgnext a')
        # print(next_pg_elems)
        # Next page link
        next_pg_link  = next_pg_elems[0].get('href')
        url = next_pg_link
        # print(next_pg_link)
    except IndexError:
        print(url)
        break

    n += 1
    print('Page %d has downloaded.' % (n))

print('Done')
