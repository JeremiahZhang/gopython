# userfile.py
#   Program to create a file of usernames in batch mode.

def main():
    print("This program creates a file of usernames from a")
    print("file of names.")

    # Get the file names
    infile_name = input("What file are the names in?")
    outfile_name = input("What file should the usernames go in?")

    # Open the files
    infile = open(infile_name, "r")
    outfile = open(outfile_name, "w")

    # Process each line of the input file
    for line in infile:
        # Get the first and last names from line
        first, last = line.split()
        # Create the username
        uname = (first[0] + last[:7]).lower()
        # Write it to the output file
        print(uname, file=outfile)

    # Close both files
    infile.close()
    outfile.close()

    print("Usernames have been written to {}.".format(outfile_name))

if __name__ == '__main__':
    main()
