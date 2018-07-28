import urllib.request, urllib.error
from bs4 import BeautifulSoup

class AppURLopener(urllib.request.FancyURLopener):
    version = 'Mozilla/5.0'

url = input('Enter - ')
opener = AppURLopener()
html = opener.open(url).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('a')
for tag in tags:
    # look at the parts of a tag
    print('TAG:', tag)
    print('URL', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
