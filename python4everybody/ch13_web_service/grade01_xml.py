import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

while True:
    url = input('Enter location: ')
    if len(url) < 1: break

    print('Retrieving {}'.format(url))
    url_handle = urllib.request.urlopen(url)
    data = url_handle.read()
    print('Retrieved {} characters'.format(len(data)))
    # print(data.decode())
    tree = ET.fromstring(data)

    counts = tree.findall('.//count')
    print('Count : {}'.format(len(counts)))
    sum = 0
    for count in counts:
        sum += int(count.text)

    print('Sum: {}'.format(sum))
