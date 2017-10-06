# all_name_value.py
#   A program to calculate the total value of all the names.
#   Such as "John Marvin Zelle".

"""
This program is to calculate the total value of
the whole name.

Please enter the whole name: John Zelle
The total value of the whole name john zelle is 107
"""

def main():
    print("This program is to calculate the total value of")
    print("the whole name.")
    print()

    # Input
    whole_name = input("Please enter the whole name: ")
    whole_name = whole_name.lower()
    total_value = 0

    # Processing
    for word in whole_name.split():
        for i in range(len(word)):
            letter_value = ord(word[i]) - 96
            total_value += letter_value

    # Output
    print("The total value of the whole name {0} is {1}"
          .format(whole_name, total_value))

if __name__ == '__main__':
    main()
