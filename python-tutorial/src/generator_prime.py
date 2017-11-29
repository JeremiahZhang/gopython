import math

def get_primes(number):
    while True:
        if is_prime(number):
            yield number

        number += 1

def solve_numer_10():
    # Working on Project Euler #10
    """
    Project Euler problem 10
    see in projecteuler.net
    
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.
    """
    total = 2
    for next_prime in get_primes(3):
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)
            return

def is_prime(number):
    if number > 1:
        if number == 2:
            return True

        if number % 2 == 0:
            return False

        for current in range(3, int(math.sqrt(number)+1), 2):
            if number % current == 0:
                return False

        return True

    return False

def main():
    solve_numer_10()

if __name__ == '__main__':
    main()
