# printfile.py
#   Prints a file to the screen

def main():
    fname = input("Enter filename: ")
    infile = open(fname, "r")
    data = infile.read()
    print(data)

if __name__ == '__main__':
    main()
