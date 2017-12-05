# acronym.py
#   A program to taking the first letters of the words in a phrase
#   and to make a word from them.
#   Example: RAM is an acronym for "random access memory".

def main():
    print("This program is to output an acronym for the phrase that")
    print("is typed by the user.")

    # Input
    phrase_str = input("Please enter your phrase: ")

    acronym_word = ""
    # Processing
    for word in phrase_str.split():
        acronym_word += word[0]

    acronym_words = acronym_word.upper()

    # Output
    print("The acronym of your phrase is {}.".format(acronym_words))

if __name__ == '__main__':
    main()

"""
anifacc@mint ~/Documents/gopython/Python-Programming-an-Introduction-to-CS/src/ch05 $ python3 acronym.py
This program is to output an acronym for the phrase that
is typed by the user.
Please enter your phrase: random access memory
The acronym of your phrase is RAM.
anifacc@mint ~/Documents/gopython/Python-Programming-an-Introduction-to-CS/src/ch05 $ python3 acronym.py
This program is to output an acronym for the phrase that
is typed by the user.
Please enter your phrase: learn from data
The acronym of your phrase is LFD.
anifacc@mint ~/Documents/gopython/Python-Programming-an-Introduction-to-CS/src/ch05 $ python3 acronym.py
This program is to output an acronym for the phrase that
is typed by the user.
Please enter your phrase: learn linux the hard way
The acronym of your phrase is LLTHW.
anifacc@mint ~/Documents/gopython/Python-Programming-an-Introduction-to-CS/src/ch05 $ python3 acronym.py
This program is to output an acronym for the phrase that
is typed by the user.
Please enter your phrase: learn python the hard way
The acronym of your phrase is LPTHW.
"""
