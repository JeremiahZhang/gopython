# slope.py
#   A program to calculate the slope of a line
#   through 2(non-vertical) points in 2D dimension.

def main():
    print("Please enter the coordinates of two point.")
    print("Like this each time: x, y")
    print()

    x1, y1 = eval(input("Enter the coordinate of 1st point: "))
    x2, y2 = eval(input("Enter the coordinate of 2nd point: "))

    slope = (y2 - y1) / (x2 - x1)

    print("The slope of the line is: {}.".format(slope))

main()
