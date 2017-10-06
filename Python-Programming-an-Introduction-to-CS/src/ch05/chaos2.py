# chaos2.py
#   A program to print a nicely formatted table showing
#   how the values change over time.
"""
This program illustrates a nicely formatted table.

Enter two numbers between 0~1,seperated by a comma: 0.25, 0.26
index     0.25          0.26
------------------------------
  1     0.731250      0.750360
  2     0.766441      0.730547
  3     0.698135      0.767707
  4     0.821896      0.695499
  5     0.570894      0.825942
  6     0.955399      0.560671
  7     0.166187      0.960644
  8     0.540418      0.147447
  9     0.968629      0.490255
 10     0.118509      0.974630
"""

def main():
    print("This program illustrates a nicely formatted table.")
    print()

    # Input
    x1, x2 = eval(str(input("Enter two numbers between 0~1,seperated by a comma: ")))
    # Processing
    print("{0:^5}{1:^14.2f}{2:^14.2f}".format("index", x1, x2))
    print("{0:^30}".format("-"*30))

    for i in range(10):
        x1 = 3.9 * x1 * (1 - x1)
        x2 = 3.9 * x2 * (1 - x2)
        # Output
        print("{0:^5}{1:^14.6f}{2:^14.6f}".format(i+1, x1, x2))

if __name__ == '__main__':
    main()
