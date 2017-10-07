# add_interest3.py

def add_interest(balances, rate):
    for i in range(len(balances)):
        balances[i] = balances[i] * (1 + rate)

def main():
    amounts = [1000, 2200, 800, 360]
    rate = 0.05
    add_interest(amounts, rate)
    print(amounts)

if __name__ == '__main__':
    main()
