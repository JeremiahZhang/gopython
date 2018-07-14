def main():
    file = 'C:/Users/Jeremy/Documents/vocation/gopython/python4everybody/ch07_files/mbox-short.txt'

    count = 0

    with open(file) as f:
        for line in f:
            words = line.split()
            # print('Debug:', words)
            if len(words) > 0: 
            # print('Debug:', len(words))
            # print('Debug:', words[0])
                if words[0] != 'From': 
                    continue
                print(words[1])
                count += 1

        print('There were {} lines in the file with From as the fist word.'.format(count))

if __name__ == '__main__':
    main()
