"""
>>> from recpower import rec_power
>>> rec_power(2, 5)
32
>>> from recpower import loop_power
>>> loop_power(2, 5)
32
"""

def loop_power(a, n):
    ans = 1
    for i in range(n):
        ans = ans * a

    return ans

def rec_power(a, n):
    if n == 0:
        return 1
    else:
        factor = rec_power(a, n//2)
        if n%2 == 0:
            return factor * factor
        else:
            return factor * factor * a
