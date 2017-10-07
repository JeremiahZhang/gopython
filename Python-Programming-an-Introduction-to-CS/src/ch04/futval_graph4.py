from graphics import GraphWin
from graphics import Text
from graphics import Point
from graphics import Rectangle

def create_labeled_window():
    window = GraphWin("Investment Growth Chart", 320, 240)
    window.setBackground("white")
    window.setCoords(-1.75, -200, 11.5, 10400)

    Text(Point(-1, 0), "0.0K").draw(window)
    Text(Point(-1, 2500), "2.5K").draw(window)
    Text(Point(-1, 5000), "5.0K").draw(window)
    Text(Point(-1, 7500), "7.5K").draw(window)
    Text(Point(-1, 10000), "10.0K").draw(window)

    return window

def draw_bar(window, year, height):
    bar = Rectangle(Point(year, 0), Point(year+1, height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(window)

def main():
    print("This program plots the growth of a 10-year investment.")
    print()

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annualized interest rate: "))

    win = create_labeled_window()
    
    draw_bar(win, 0, principal)

    for year in range(1, 11):
        principal = principal * (1 + apr)
        draw_bar(win, year, principal)

    input("Press <Enter> to quit.")

    win.close()

if __name__ == '__main__':
    main()
