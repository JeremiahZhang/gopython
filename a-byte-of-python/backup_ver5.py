import os
import time
import zipfile


def get_all_file_paths(directory):
	file_paths = []
	for root, directories, files in os.walk(directory):
		for filename in files:
			filepath = os.path.join(root, filename)
			file_paths.append(filepath)
	
	return file_paths

source = "C:\\Users\\Jeremy\\Documents\\Wording"

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

file_paths = get_all_file_paths(source)
print('Following files will be zipped:')
for file_name in file_paths:
	print(file_name)

with zipfile.ZipFile(target, 'w') as zip:
		for file in file_paths:
			zip.write(file)

print(zip.namelist)
print('Successfully backed up!!!')

# https://www.geeksforgeeks.org/working-zip-files-python/
# http://pymotw.com/2/zipfile/