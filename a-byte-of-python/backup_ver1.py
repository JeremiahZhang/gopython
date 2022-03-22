import os
import time

# 1. The files and dirctories to be 
# backed up are specified in a list.
source = ["C:\\Users\\Jeremy\\Documents\\Wording"]

# 2. The backup must be stored in 
# main backup directory
target_dir = 'C:\\Users\\Jeremy\\Documents\\MyProject\\Backup'

# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current
#    date and time
target = target_dir + os.sep + \
		 time.strftime('%Y%m%d%H%M%S') + '.zip'

# Creat target directory if it is not present
if not os.path.exists(target_dir):
	os.mkdir(target_dir)

# 5. Use the zip command to put the files in a zip 
# Here we need to install Zip and add
# 'C:\Program Files (x86)\GnuWin32\bin' to
# enviroment variables in Windows
zip_command = 'zip -r {0} {1}'.format(target, 
									  ' '.join(source))

# Run
print('Zip command is:')
print(zip_command)
print('Running')
if os.system(zip_command) == 0:
	print('Successful backup to', target)
else:
	print('Backup FAILED')