def by_freq(pair):
    return pair[1]

def main():
    print("This program analyzes word frequency in a file")
    print("and prints a report on the n most frequent words.\n")

    # get the sequence of words from the file
    f_name = input("File to analyze: ")
    text = open(f_name, 'r').read()
    text = text.lower()

    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_{|}~`':
        text = text.replace(ch, ' ')

    words = text.split()

    # construct a dictionary of word counts
    counts ={}
    for w in words:
        counts[w] = counts.get(w, 0) + 1

    # output analysis of n most frequent words.
    n = eval(input("Output analysis of how many words? "))

    items = list(counts.items())
    items.sort() # alphabeta order
    items.sort(key=by_freq, reverse=True) # words frequecy

    for i in range(n):
        word, count = items[i]
        print("{0:<15}{1:>5}".format(word, count))

if __name__ == '__main__': main()
