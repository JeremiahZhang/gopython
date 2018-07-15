def main():
    fname = input('Enter a file: ')
    file = 'C:/Users/Jeremy/Documents/vocation/gopython/python4everybody/ch08_lists/remeo.txt'
    if len(fname) < 1: 
        # print('Debug')
        fname = file    

    wordlist = list()

    try:
        # print('Debug')
        with open(fname) as f:
            # print('Debug word.')
            for line in f:
                line = line.lower()
                words = line.split()
                for word in words:
                    # print('Debug word.')
                    if word in wordlist: continue
                    wordlist.append(word)
    except:
        print('{} is not found. Please enter a correct file name!'.format(fname))

    wordlist.sort()
    print(wordlist)

if __name__ == '__main__':
    main()
