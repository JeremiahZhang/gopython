# -*- coding: utf-8 -*-

def main():
    '''
    Exercise 3: Sometimes when programmers get bored or want 
    to have a bit of fun, they add a harmless Easter Egg to 
    their program Modify the program that prompts the user 
    for the file name so that it prints a funny message when 
    the user types in the exact file name "na na boo boo". 
    The program should behave normally for all other files 
    which exist and don't exist. Here is a sample execution
    of the program:

    python egg.py
    Enter the file name: mbox.txt
    There were 1797 subject lines in mbox.txt

    python egg.py
    Enter the file name: missing.tyxt
    File cannot be opened: missing.tyxt

    python egg.py
    Enter the file name: na na boo boo
    NA NA BOO BOO TO YOU - You have been punk'd!
    '''

    fname = input('Enter the file name: ')
    count = 0

    if fname.find('.') == -1:
        fname = fname.upper()
        print('{} - You have been punkd!'.format(fname))
        exit()

    try:
        with open(fname) as fh:
            for line in fh:
                line = line.rstrip()
                if not line.startswith('Subject'): continue
                count = count + 1

            print('There were {} subject lines in {}'.format(count, fname))
    except:
        print('File cannot be opened:', fname)
        exit()

if __name__ == '__main__':
    main()
