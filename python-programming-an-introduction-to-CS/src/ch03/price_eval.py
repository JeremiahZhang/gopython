# price_eval.py

def main():
    print("Please enter the average ROE, net equity, stocks amount.")
    print("Enter 3 number, seperated by a comma.")

    # Average ROE of ten years.
    # The latest net equity.
    # The latest stocks amount.
    for i in range(10):
        avg_roe, net_equity, stock_amount = eval(input("Enter here: "))

        eval_price = avg_roe / 10 * net_equity / stock_amount

        buy_price = 0.5 * eval_price
        sell_price1 = eval_price
        sell_price2 = 1.1 * eval_price

        print("The buying price is {}.".format(buy_price))
        print("When the price is above, you maybe need to buy it.")
        print()
        print("When the price has rising to {}, you maybe think to sell.".format(sell_price1))
        print("The sell price 01(100%) is {}.".format(sell_price1))
        print()
        print("When the price has rising to {}, you must sell it.".format(sell_price2))
        print("The sell_price 02(110%) is {}.".format(sell_price2))

main()
