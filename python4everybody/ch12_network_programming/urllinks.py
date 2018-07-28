import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
# import ssl

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

class AppURLopener(urllib.request.FancyURLopener):
    version = 'Mozilla/5.0'

url = input('Enter - ')
# urllib.error.HTTPError: HTTP Error 403: Forbidden
# html = urllib.request.urlopen(url, context=ctx).read()
opener = AppURLopener()
html = opener.open(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
