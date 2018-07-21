# Search for lines that start with 'F', followed by
# 2 characters, followed by 'm:'
import re
fname = 'C:/Users/Jeremy/Documents/vocation/gopython/python4everybody/ch07_files/mbox-short.txt'

with open(fname) as fh:
    for line in fh:
        line = line.rstrip()
        if re.search('^F..m:', line):
            print(line)
