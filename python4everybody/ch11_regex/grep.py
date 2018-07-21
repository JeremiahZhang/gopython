import re

def main():

    """
    Exercise 1: Write a simple program to simulate the operation of 
    the grep command on Unix. Ask the user to enter a regular 
    expression and count the number of lines that matched the 
    regular expression:
    $ python grep.py
    Enter a regular expression: ^Author
    mbox.txt had 1798 lines that matched ^Author

    $ python grep.py
    Enter a regular expression: ^X-
    mbox.txt had 14368 lines that matched ^X-

    $ python grep.py
    Enter a regular expression: java$
    mbox.txt had 4218 lines that matched java$
    """
    exp = input('Enter a regular expression: ')
    fname = 'mbox.txt'

    count = 0
    with open(fname) as fh:
        for line in fh:
            line = line.rstrip()
            if re.search(exp, line):
                count += 1

    print('{0} had {1} lines that matched {2}'.format(fname, count, exp))

if __name__ == '__main__':
    main()
