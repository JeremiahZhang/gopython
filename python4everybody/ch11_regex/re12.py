# Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39772
# Search for lines that start with 'Details: rev='
# followed by numbers and '.'
# Then print the number if it is greater than zero

import re
fname = 'C:/Users/Jeremy/Documents/vocation/gopython/python4everybody/ch07_files/mbox-short.txt'

with open(fname) as fh:
    for line in fh:
        line = line.rstrip()
        x = re.findall('^Details:.*rev=([0-9.]+)', line)
        if len(x): print(x)
