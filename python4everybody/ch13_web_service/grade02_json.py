import urllib.request, urllib.parse, urllib.error
import json

while True:
  url = input('Enter location: ')
  if len(url) < 1: break

  print('Retrieving', url) 
  uh = urllib.request.urlopen(url)
  data = uh.read()
  print('Retrieved', len(data), 'characters')

  info = json.loads(data)
  comments = info['comments']
  print('Count', len(comments))

  sum = 0
  for item in comments:
    sum += item['count']
  print('Sum', sum)
