# caesar_cipher2.py
#   A program that can encodo and decode Caesar Ciphers.
#   It can shift in a circular fashion where the next character
#   after "z" is "a".
#       Hint: make a string containing all the characters of
#             your alphabet and use positions in this string
#             as your code.
#             You do not have to shift "z" into "a" just make
#             sure that you use a circular shift over the entire
#             sequence of characters in your alphabet string.
"""
This is an improved program of Caesar cipher.

Please enter your string of plaintext: zzaabbzz
Please enter the key value: 1
The result is aabbccaa.
"""

def main():
    print("This is an improved program of Caesar cipher.")
    print()

    # Input
    input_str = input("Please enter your string of plaintext: ")
    key_value = eval(input("Please enter the key value: "))

    # Processing
    encoded_str = ""
    alphabet_string = "abcdefghijklmnopqrstuvwxyz"

    for i in range(len(input_str)):
        ch_in_strs = input_str[i]
        ch_idx = alphabet_string.find(ch_in_strs)
        encoded_idx = ch_idx + key_value

        if encoded_idx >= len(alphabet_string):
            encoded_idx = encoded_idx - len(alphabet_string)

        encoded_ch = alphabet_string[encoded_idx]
        encoded_str += encoded_ch

    # Output
    print("The result is {}.".format(encoded_str))

if __name__ == '__main__':
    main()
