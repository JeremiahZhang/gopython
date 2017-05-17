# -*- coding: utf-8 -*-

"""
Binary search pseudocode from Khan Academy course Algorithm

1. Let min = 0 and max = n - 1.
2. Compute guess as the average of max and min, rounded down(so that it is an integer).
3. If list[guess] equals target, then stop. You find it! Return guess.
4. If the guess was to low, that is, list[guess] < target, then set min = guess + 1.
5. Otherwise, the guess was too high. Set max = guess - 1.
6. Go back to step 2.

Modified:(if the target number is not present)

1. Let min = 0 and max = n-1.
2. If max < min, then stop: target is not present in list. Return -1.
3. Compute guess as the average of max and min, rounded down(so that it is an integer).
5. If list[guess] equals target, then stop. You find it! Return guess.
5. If the guess was to low, that is, list[guess] < target, then set min = guess + 1.
6. Otherwise, the guess was too high. Set max = guess - 1.
7. Go back to step 2.
"""

def binary_search(num_list, target_num):
    min = 0
    max = len(num_list) - 1

    while True:
        if max < min:
            return -1

        guess = (min + max)/2

        if num_list[guess] == target_num:
            return guess
        elif num_list[guess] < target_num:
            min = guess + 1
        else:
            max = guess - 1fa

def main():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, \
             59, 61, 67, 71, 73, 79, 83, 89, 97];
    result = binary_search(primes, 73)
    print "Found prime at index %d" % result

if __name__ == '__main__':
    main()