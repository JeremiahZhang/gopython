import math

def get_primes(input_list):
    result_list = list()
    for num in input_list:
        if is_prime(num):
            result_list.append(num)

    return result_list

def get_primes_simplifier(input_list):
    return [num for num in input_list if is_prime(num)]

def is_prime(num):
    if num > 1:
        if num == 2:
            return True

        if num % 2 == 0:
            return False

        for current in range(3, int(math.sqrt(num) + 1), 2):
            if num % current == 0:
                return False

        return True
    return False

def main():
    numbers = [x for x in range(20)]
    primes = get_primes(numbers)
    print("Primes_1: {}".format(primes))
    primes2 = get_primes_simplifier(numbers)
    print("Primes_2: {}".format(primes2))

if __name__ == '__main__':
    main()
