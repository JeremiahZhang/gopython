# coffee_cost.py
#   A program that calculates the cost of an order.
#   The Konditorei coffe shop sells coffee at $10.5
#   a pound + the cost of shipping.
#   Each order ships for $0.86 per pound + $1.5
#   fixed cost for overhead.

def main():
    print("Please input the pound of an order.")
    print()

    pound = eval(input("Enter the pound here: "))

    cost = (10.5 + 0.86) * pound + 1.50

    print("The cost of an order is {} dollars.".format(cost))

main()
