# futval_graph.py

from graphics import GraphWin
from graphics import Text
from graphics import Point
from graphics import Rectangle

def main():
    # Introduction
    print("This program plots the growth of a ten-year investment.")

    # Get principal and interest rate(annualized interest rate)
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annualized interest rate: "))

    # Creat a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")

    Text(Point(20, 230), "0.0K").draw(win)
    Text(Point(20, 180), "2.5K").draw(win)
    Text(Point(20, 130), "5.0K").draw(win)
    Text(Point(20, 80), "7.5K").draw(win)
    Text(Point(20, 30), "10.0K").draw(win)

    # Draw bar for initial principal
    height = principal * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230 - height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # Draw bars for successive years
    for year in range(1, 11):
        # Calculate value for the next year
        principal = principal * (1 + apr)
        # draw bar for this value
        x_low_left = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(x_low_left, 230), Point(x_low_left+25, 230-height))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    input("Press <Enter> to quit")
    win.close()

if __name__ == '__main__':
    main()
