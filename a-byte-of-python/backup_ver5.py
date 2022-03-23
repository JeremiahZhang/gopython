import os
import time
import zipfile

source = ["C:\\Users\\Jeremy\\Documents\\Wording"]

target_dir = 'C:\\Users\\Jeremy\\Documents\\MyProject\\Backup'

if not os.path.exists(target_dir):
	os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

if not os.path.exists(today):
	os.mkdir(today)
	print('Successfully created directory', today)

comment = input('Enter a comment --> ')

if len(comment) == 0:
	target = today + os.sep + now + '.zip'
else:
	target = today + os.sep + now + '_' + \
	         comment.replace(' ', '_') + '.zip'

print('Running:')
print('Following files will be zipped:')
for files in source:

with zipfile.ZipFile(target, 'w') as zip:
		zip.write(file)

print('Successfully backed up!!!')

# https://www.geeksforgeeks.org/working-zip-files-python/