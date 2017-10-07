# word_count.py
#   A program analyzes a file to determine the number of lines,
#       words, and charaters contained therein.
"""
---
File contants:
    $ cat test.txt
    This is a test text file.

    to testing the chapter 05 programming exercise 15.
---
Testing:
$ python3 word_count.py
This program accept a file name as input and
then print three numbers showing the count of lines,
words, and charaters in the file.

Please enter your file name: test.txt
1
['This', 'is', 'a', 'test', 'text', 'file', '']
2
['']
3
['to', 'testing', 'the', 'chapter', '05', 'programming', 'exercise', '15', '']
The number of lines is 3.
The number of words is 17.
The number of charaters is 61.
---
Need to debug later.
"""


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
    # print(infile.read())

    for line in infile.readlines():
        num_lines += 1
        words_in_line = re.split('[\W+]', line[:-1])
        words_list.extend(words_in_line)

        print(num_lines)
        print(words_in_line)

        for word in words_in_line:
            num_charaters += len(word)

        words_in_line = []

    num_words = len(words_list)

    infile.close()

    # Output
    print("The number of lines is {}.".format(num_lines))
    print("The number of words is {}.".format(num_words))
    print("The number of charaters is {}.".format(num_charaters))

if __name__ == '__main__':
    main()
