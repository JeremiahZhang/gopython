"""
Revise a previous program as follows: Read and parse the "From" lines and pull out the addresses from the line. 
Count the number of messages from each person using a dictionary.

After all the data has been read, print the person with the most commits by creating a list of (count, email) 
tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
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
                    counts[words[1]] = counts.get(words[1], 0) + 1

        lst = list()
        for key, val in counts.items():
            lst.append((val, key))

        # print('debugging')
        lst.sort(reverse=True)
        val, key = lst[0]
        print(key, val)
        # print('debugging')
    except:
        print('File is not found', fname)
        exit()

if __name__ == '__main__':
    main()
