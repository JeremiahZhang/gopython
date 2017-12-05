#! /usr/bin/python3
# download_xkcd.py - Downloads every single XKCD comic.

import os
import requests
import bs4

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True) # store comics in ./xkcd

while not url.endswith('#'):
    print('Downloading page {} ...'.format(url))
    # Todo: Download the page
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # Todo: Find the URL of the comic image
    # <div id="comic"> ...
    #     <img src="//imgs.xkcd.com/comics/solar_panels.png" ....>
    comic_elem = soup.select('#comic img') # here you need add img
    
    if comic_elem == []:
        print('Could not find comic image.')
    else:
        try:
            comic_url = 'http:' + comic_elem[0].get('src') # here you need to see source info
            # Todo: Download the image
            print('Downloading image {} ...'.format(comic_url))
            res = requests.get(comic_url)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            # skip this comic
            # <a rel="prev" href="/1923/" accesskey="p">&lt; Prev</a>
            prev_link = soup.select('a[rel="prev"]') # page source info
            url = 'http://xkcd.com' + prev_link.get('href')
            continue
        # Todo: Save the image to ./xkcd
        image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)

        image_file.close()

    # Todo: Get the Prev button's url
    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prev_link.get('href')

print('Done.')