def fib(n):     # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print a
        a, b = b, a+b

def fib2(n):    # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b

    return result

def main():
    n = int(raw_input("Please enter the number to write"
                        " Fibonacci series: "))
    fib(n)

if __name__ == '__main__':
    main()
