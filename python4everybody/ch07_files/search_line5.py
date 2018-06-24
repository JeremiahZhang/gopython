def main():
    count = 0
    with open('mbox-short.txt') as f:
        for line in f:
            line = line.rstrip()
            if not line.startswith('From '): continue
            words = line.split()
            count += 1
            print(words[2])

        print('Count:', count)

if __name__ == '__main__':
    main()
