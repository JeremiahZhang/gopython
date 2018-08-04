import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
pos = int(input('Enter position: '))

# urllib.error.HTTPError: HTTP Error 403: Forbidden
for i in range(count+1):
    print('Retrieving:', url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[pos-1].get('href', None)

# for tag in tags:
#     print('Retrieving: ', tag.get('href', None))
#         # print('Contents:', tag.contents[0])
