# File: chaos.py (.py: python module or script)
# A simple program illustrating chaotic behavior.

def main():
    print("This program illustrates a chaotic function.")
    x = eval(str(input("Enter a number between 0 and 1: ")))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)

main()
