poem = '''A Psalm of David

The Lord is my shepherd; 
I shall not want.
He makes me lie down in green pastures.
'''

# Open for 'w'riting
f = open('poem.txt', 'w')
# Write text to file
f.write(poem)
# Close the file
f.close()

# If no mode is specified,
# 'r'ead mode is assumed by default
f = open('poem.txt')
while True:
	line = f.readline()
	# Zero length indicates EOF
	if len(line) == 0:
		break
	# The `line` already has a newline
	# at the end of each line
	# since it is reading from a file.
	print(line, end='')

print('---')
print('Readline finished.')

# Close the file
f.close()