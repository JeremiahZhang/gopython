# caesar_cipher.py
#   A program that can encodo and decode Caesar Ciphers.
#   Example:
#       input:
#           - word: "Sourpuss"
#           - key value: 2
#       output:
#           - word: "Uqwtrwuu"
"""
This program is to encode Caesar ciphers.
The input of this program are a string of plaintext
and the value of the key.

Please enter your string of plaintext: Sourpuss
Please enter the key value: 2
The result is Uqwtrwuu.
"""

def main():
    print("This program is to encode Caesar ciphers.")
    print("The input of this program are a string of plaintext")
    print("and the value of the key.")
    print()

    # Input
    strings = input("Please enter your string of plaintext: ")
    key_value = eval(input("Please enter the key value: "))

    encoded_str = ""

    # Processing
    for i in range(len(strings)):
        encoded_letter = chr(ord(strings[i]) + key_value)
        encoded_str += encoded_letter

    # Output
    print("The result is {}.".format(encoded_str))

if __name__ == '__main__':
    main()
