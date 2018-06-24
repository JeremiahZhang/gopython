# Using try, except

def main():
    fname = input('Enter the file name:')
    count = 0

    try:
        with open(fname) as f:
            for line in f:
                if line.startswith('Subject:'):
                    count = count + 1
        print('There were {} subject lines in {}'.format(count, fname))
    except:
        print('File can not be found and opened: ', fname)
        exit()

if __name__ == '__main__':
    main()
