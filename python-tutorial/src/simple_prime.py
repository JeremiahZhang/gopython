def find_prime(number):
    """
    Find primes in range 2-number
    """
    for n in range(2, number+1):
        for x in range(2, n):
            if n % x == 0:
                print("{0} = {1} * {2}".format(n, x, n/x))
                break
        else:
            # loop fell through without finding a factor
            print("{} is a prime number".format(n))

def main():
    num = int(raw_input("please enter a number: "))
    print("Find primes in 2-{} range".format(num))
    find_prime(num)

if __name__ == '__main__':
    main()
