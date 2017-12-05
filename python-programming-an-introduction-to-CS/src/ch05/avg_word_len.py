# avg_word_len.py
#   A program to calculate the average word length in
#   a sentence entered by usr.
"""
This program is to calculate the average word length
in a sentence.

Please enter your sentence: hello jeremy welcome to Linux word
The average word length is 4.833333333333333.
"""

def main():
    print("This program is to calculate the average word length")
    print("in a sentence.")

    print()

    # Input
    sentence = input("Please enter your sentence: ")

    # Process
    avg_length = 0
    sentence_splited = sentence.split()
    for word in sentence_splited:
        avg_length += len(word)

    avg_length /= len(sentence_splited)

    # Output
    print("The average word length is {}.".format(avg_length))

if __name__ == '__main__':
    main()
