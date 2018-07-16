def main():
    fname = input('Enter a file name: ')
    if len(fname) < 1: 
        fname = 'C:/Users/Jeremy/Documents/vocation/gopython/python4everybody/ch07_files/mbox-short.txt'

    counts = dict()

    try:
        with open(fname) as fh:
            # print('Debug open fname')
            for line in fh:
                # print('Debug for loop')
                line = line.rstrip()
                if line.startswith('From '):
                    # print('Debug starstwith')
                    words = line.split()
                    # print(words)
                    counts[words[2]] = counts.get(words[2], 0) + 1
        print(counts)
    except:
        print('File can not be found and opened: ', fname)
        exit()


if __name__ == '__main__':
    main()
