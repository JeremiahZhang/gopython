import re

def main():
    """
    Exercise 2: Write a program to look for lines of the form
    `New Revision: 39772`
    and extract the number from each of the lines using 
    a regular expression and the findall() method. 
    Compute the average of the numbers and print out the average.
    """
    fname = input('Enter file: ')
    if len(fname) < 1:
        fname = 'C:/Users/Jeremy/Documents/vocation/gopython/python4everybody/ch07_files/mbox-short.txt'

    try:
        count = 0
        total = 0
        with open(fname) as fh:
            for line in fh:
                line = line.rstrip()
                lst = re.findall('\S*New Revision: ([0-9.]+)', line)
                for x in lst:
                    x = float(x)
                    count += 1
                    total += x
        avg = total / count
        print(avg)
    except:
        print('Cannot find file', fname)
        exit()

if __name__ == '__main__':
    main()
