# search through line 
# rstrip the newline character

def main():
    count = 0
    with open('mbox-short.txt') as fhand:
        for line in fhand:
            line = line.rstrip()
            if line.startswith('From:'):
                count += 1
                print(line)

        print('The "From:" line Count:', count)

if __name__ == '__main__':
    main()
