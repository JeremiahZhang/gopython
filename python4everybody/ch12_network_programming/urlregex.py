# Search for lines that start with From 
# and have an at sign

import urllib.request, urllib.parse, urllib.error
import re

class AppURLopener(urllib.request.FancyURLopener):
    version = 'Mozilla/5.0'    

url = input('Enter - ')
# html = urllib.request.urlopen(url).read()
opener = AppURLopener()
html = opener.open(url).read()
links = re.findall(b'href="(http://.+?)"', html)
for link in links:
    print(link.decode())
