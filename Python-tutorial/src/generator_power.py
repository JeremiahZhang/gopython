import math

from fun_with_prime import is_prime

"""
find the smallest prime number greater than successive powers of a number
 (i.e. for 10, we want the smallest prime
 greater than 10, then 100, then 1000, etc.).
"""

def print_successive_primes(iterations, base=10):
    # A generator function like normal function
    # can be assigned to a viriable

    prime_generator = get_primes(base)

    prime_generator.send(None)

    for power in range(iterations):
        print(prime_generator.send(base ** power))

def get_primes(number):
    while True:
        if is_prime(number):
            number = yield number

        number += 1

def main():
    print_successive_primes(2, 10)

if __name__ == '__main__':
    main()
