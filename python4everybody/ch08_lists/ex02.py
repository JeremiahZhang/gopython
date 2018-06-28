def main():
    file = 'C:/Users/Jeremy/Documents/vocation/gopython/python4everybody/ch07_files/mbox-short.txt'

    with open(file) as f:
        for line in f:
            words = line.split()
            # print('Debug:', words)
            if len(words) > 0: 
            # print('Debug:', len(words))
            # print('Debug:', words[0])
                if words[0] != 'From': 
                    continue
                print(words[2])

if __name__ == '__main__':
    main()
