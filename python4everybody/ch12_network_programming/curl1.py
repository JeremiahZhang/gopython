import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()

fhand = open('cover3.jpg', 'wb')
print('Writing...')
fhand.write(img)
fhand.close()
print('Finished. File has been downloaded.')
