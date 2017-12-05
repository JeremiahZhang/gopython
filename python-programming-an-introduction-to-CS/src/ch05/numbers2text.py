# numbers2text.py
#   A program to convert a sequence of Unicode numbers into
#       a string of text.

def main():
    print("This program converts a sequence of Unicode numbers into")
    print("the string of text that it represents!\n")

    # Get the mess to encdoe
    in_string = input("Please enter the Unicode-encoded message: ")
    # Loop through each substring and build Unicode message
    message = ""
    for num_str in in_string.split():
        # Convert digits to a number
        code_num = eval(num_str)
        message = message + chr(code_num) # concatentate character to message

    print("\nThe decoded message is: {}.".format(message))

if __name__ == '__main__':
    main()
