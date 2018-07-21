import string

def main():
    """
    Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency.
     Your program should convert all the input to lower case and only count the letters a-z. 
     Your program should not count spaces, digits, punctuation, or anything other than the 
     letters a-z. Find text samples from several different languages and see how letter 
     frequency varies between languages. 
    """
    fname = input('Enter a file name: ')
    if len(fname) < 1:
        fname = 'C:/Users/Jeremy/Documents/vocation/gopython/python4everybody/ch07_files/mbox-short.txt'

    counts = dict()
    try:
        with open(fname) as fh:
            for line in fh:
                line = line.translate(str.maketrans('', '', string.punctuation))
                line = line.lower()
                words = line.split()
                for word in words:
                    for ch in word:
                        counts[ch] = counts.get(ch, 0) + 1

        lst = list()
        for key, val in counts.items():
            lst.append((val, key))

        lst.sort(reverse=True)
        for (val, key) in lst[:]:
            print(key, val)
    except:
        print('Cannot find file', fname)
        exit()

if __name__ == '__main__':
    main()


