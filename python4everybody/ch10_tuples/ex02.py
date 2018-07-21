"""
Exercise 2: This program counts the distribution of the hour of the 
day for each of the messages. You can pull the hour from the "From" 
ine by finding the time string and then splitting that string into 
parts using the colon character. Once you have accumulated the 
counts for each hour, print out the counts, one per line, sorted 
by hour as shown below.
python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
"""

def main():
    fname = input('Enter a file name: ')
    if len(fname) < 1:
        fname = 'C:/Users/Jeremy/Documents/vocation/gopython/python4everybody/ch07_files/mbox-short.txt'

    counts = dict()
    try:
        with open(fname) as fh:
            for line in fh:
                line = line.rstrip()
                if line.startswith('From '):
                    # print('debugging')
                    words = line.split()
                    time_str = words[5]
                    time_lst = time_str.split(':')
                    # print(time_lst)
                    hour = time_lst[0]
                    counts[hour] = counts.get(hour, 0) + 1

        # print('debugging')
        lst = list()
        for key, val in counts.items():
            lst.append((key, val))

        lst.sort()
        # print('debugging')
        for key, val in lst[:]:
            print(key, val)

    except:
        print('File is not found', fname)
        exit()

if __name__ == '__main__':
    main()
