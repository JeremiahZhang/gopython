import re

def main():
    fname = input('Enter file: ')
    if len(fname) < 1:
        # fname = 'regex_sum_42.txt'
        fname = 'regex_sum_103497.txt'

    try:
        lst = list()
        with open(fname) as fh:
            for line in fh:
                line = line.rstrip()
                numlst = re.findall('[0-9]+', line)
                for x in numlst:
                    # print('Debugging 1')
                    # print(x)
                    x = float(x)
                    # print('Debugging 2')
                    lst.append(x)

        total = sum(lst)
        print('sum =', total)
    except:
        print('Cannot find the file', fname)
        exit()

if __name__ == '__main__':
    main()
