# words_num_count.py
#   A program to count the number of words in a sentence
#   enter by the user.

def main():
    print("This program is to count the number of words in")
    print("a sentence enter by the user.")
    print()

    # Input
    sentence = input("Please enter your sentence in English: ")

    # Processing
    sen_split = sentence.split()
    num = len(sen_split)

    # Output
    print("The number of words in your sentence is {}.".format(num))

if __name__ == '__main__':
    main()
