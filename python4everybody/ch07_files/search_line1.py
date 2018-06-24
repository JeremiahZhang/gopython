# search through the lines
# ref
# https://www.py4e.com/html3/07-files

def main():
    count = 0

    with open('mbox-short.txt') as fhand:
        for line in fhand:
            if line.startswith('From:'):
                count += 1
                print(line)

    print('The "from" line count: ', count)

if __name__ == '__main__':
    main()
