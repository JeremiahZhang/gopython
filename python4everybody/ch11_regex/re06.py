# 
# Search for lines that contain 'From'
import re
fname = 'C:/Users/Jeremy/Documents/vocation/gopython/python4everybody/ch07_files/mbox-short.txt'

with open(fname) as fh:
    for line in fh:
        line = line.rstrip()
        x = re.findall('\S+@\S+', line)
        if len(x) > 0:
            print(x)
