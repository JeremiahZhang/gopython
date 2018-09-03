# The following is a simple application to 
# prompt the user for a search string, 
#call the Google geocoding API, and 
#extract information from the returned JSON.

import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    country = input('Enter country: ')
    if len(country) < 1: break

    url = serviceurl + urllib.parse.urlencode(
        {'address': country})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    # print(js)

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure to Retrieve ====')
        print('Enter a correct country name, Please.')
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, '\n', 'lng', lng)
    location = js['results'][0]['formatted_address']
    print('Country: ', location)
