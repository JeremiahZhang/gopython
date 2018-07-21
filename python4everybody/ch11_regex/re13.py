# Search for lines that start with From and a character
# followed by a two digit number between 00 and 99 followed by ':'
# Then print the number if it is greater than zero
import re
fname = 'C:/Users/Jeremy/Documents/vocation/gopython/python4everybody/ch07_files/mbox-short.txt'

with open(fname) as fh:
    for line in fh:
        line = line.rstrip()
        x = re.findall('^From .* ([0-9][0-9]):', line)
        if len(x): print(x)
