# word_count.py
#   A program analyzes a file to determine the number of lines,
#       words, and charaters contained therein.

import re

def main():
    print("This program accept a file name as input and")
    print("then print three numbers showing the count of lines,")
    print("words, and charaters in the file.")
    print()

    # Input
    fname = input("Please enter your file name: ")

    # Processing
    num_lines = 0
    num_words = 0
    num_charaters = 0

    # Store words to calculate the number of words
    words_list = []

    infile = open(fname, "r")

    for line in infile.readlines():
        num_lines += 1
        words_in_line = re.split('', line)
        words_list.extend(words_in_line)

        print(num_lines)
        print(words_in_line)

        for word in words_in_line:
            num_charaters += len(word)

        words_in_line = []

    num_words = len(words_list)

    # Output
    print("The number of lines is {}.".format(num_lines))
    print("The number of words is {}.".format(num_words))
    print("The number of charaters is {}.".format(num_charaters))

if __name__ == '__main__':
    main()
