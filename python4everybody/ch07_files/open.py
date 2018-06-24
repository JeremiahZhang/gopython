# open file 
# ref https://www.py4e.com/html3/07-files

count = 0

with open('mbox-short.txt') as fhand:
    for line in fhand:
        count += 1

print('Line Count: ', count)
