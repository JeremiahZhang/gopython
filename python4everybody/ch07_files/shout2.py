# -*- coding: utf-8 -*- 

def main():
    '''
    Exercise 2: Write a program to prompt for a file name, 
    and then read through the file and look for lines of 
    the form:

    X-DSPAM-Confidence:0.8475
    Enter the file name: mbox.txt
    Average spam confidence: 0.894128046745

    Enter the file name: mbox-short.txt
    Average spam confidence: 0.750718518519
    '''
    fname = input('Enter the file name: ')
    count = 0
    accum = 0

    try:
        with open(fname) as f:
            for line in f:
                line = line.rstrip()
                if not line.startswith('X-DSPAM-Confidence:'): continue

                count = count + 1
                for t in line.split():
                    try:
                        accum += float(t)
                    except:
                        pass

        avg = accum / count
        print('Average spam confidence: {0:.12}'.format(avg))
    except:
        print('Enter the right file name, Please!!!')

if __name__ == '__main__':
    main()
