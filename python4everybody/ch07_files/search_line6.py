# Letting the usr choose the file name

def main():
    fname = input('Enter the file name: ')
    count = 0
    with open(fname) as f:
        for line in f:
            line = line.rstrip()
            if line.startswith('Subject:'):
                count = count + 1
        print('There were', count, 'subject lines in', fname)

if __name__ == '__main__':
    main()
