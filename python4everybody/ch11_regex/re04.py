# Search for lines that start with From and have an at sign
import re
fname = 'C:/Users/Jeremy/Documents/vocation/gopython/python4everybody/ch07_files/mbox-short.txt'

with open(fname) as fh:
    for line in fh:
        line = line.rstrip()
        if re.search('^From:.+@', line):
            print(line)
