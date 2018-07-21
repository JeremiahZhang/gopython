# Search for lines that start with 'X' followed by
# any non whitespace charaters and ':'
# followed by a space and any number.
# The number can include a decimal.
import re
fname = 'C:/Users/Jeremy/Documents/vocation/gopython/python4everybody/ch07_files/mbox-short.txt'

with open(fname) as fh:
    for line in fh:
        line = line.rstrip()
        if re.search('^X\S*: [0-9.]+', line):
            print(line)
