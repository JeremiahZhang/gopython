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
                    words = line.split()
                    usr, addr = words[1].split('@')
                    counts[addr] = counts.get(addr, 0) + 1
        print(counts)
    except:
        print('File cannot be found', fname)
        exit()

if __name__ == '__main__':
    main()
