# -*- coding: utf-8 -*-

'''
Exercise 1 of Chapter 7 files.
Exercise 1: Write a program to read through a file and 
print the contents of the file (line by line) all in upper case.
'''

def main():
    fname = input('Enter the file name: ')

    try:
        with open(fname) as f:
            for line in f:
                line = line.upper()
                line = line.rstrip()
                print(line)
    except:
        print('File cannot be opened: ', fname)
        exit()

if __name__ == '__main__':
    main()
