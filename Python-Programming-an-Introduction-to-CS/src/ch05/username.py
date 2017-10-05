# username.py
#   Simple string processing program to generate usernames.

def main():
    print("This program generates computer usernames. \n")

    # Get usr's first and last names.
    first = input("Please enter your first name (all lowercase): ")
    last = input("Please enter your last name (all lowercase): ")

    # Concatenate first initial with 7 chars of the last name.
    uname = first[0] + last[:7]

    # Output the username
    print("Your username is: {}.".format(uname))

if __name__ == '__main__':
    main()
