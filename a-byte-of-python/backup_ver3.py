import os
import time

source = ["C:\\Users\\Jeremy\\Documents\\Wording"]

target_dir = 'C:\\Users\\Jeremy\\Documents\\MyProject\\Backup'

if not os.path.exists(target_dir):
	os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

if not os.path.exists(today):
	os.mkdir(today)
	print('Successfully created directory', today)

comment = input('Enter a comment -->:')

if len(comment) == 0:
	target = today + os.sep + now + '.zip'
else:
	target = today + os.sep + now + '_' + \
	         comment.replace(' ', '_') + '.zip'

zip_command = "zip -r {0} {1}".format(target,
	                                  ' '.join(source))

# Run
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
	print('Successful backup to', target)
else:
	print('Failed!!!')