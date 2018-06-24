def main():
    file = 'C:/Users/Jeremy/Documents/vocation/gopython/python4everybody/ch07_files/mbox-short.txt'

    with open(file) as f:
        for line in f:
            line = line.rstrip()
            # 'From ' differ 'From'
            if not line.startswith('From '): continue
            words = line.split()
            print(words[2])

if __name__ == '__main__':
    main()
