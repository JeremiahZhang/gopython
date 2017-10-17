def loop_fib(n):
    curr = 1
    prev = 1

    for i in range(n-2):
        curr, prev = curr+prev, curr

    return curr

def rec_fib(n):
    if n < 3:
        return 1
    else:
        return rec_fib(n-1) + rec_fib(n-2)

def main():
    # fab1 = loop_fib(50000) # time 0.44s
    # print(fab1)

    fab2 = rec_fib(50000)
    print(fab2)
    # RecursionError: maximum recursion depth exceeded in comparison
    # maximum 1,000 times, how to change?

if __name__ == '__main__':
    main()
