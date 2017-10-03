# fibo_num.py
#   A program to compute the nth fabonacci number where n
#   is a value input by the user.
#   1, 1, 2, 3, 5, 8, ...
#   if n = 6, then the result is 8.

def main():
    print("Please enter the number n to get the nth fabonacci number.")

    n = eval(input("Enter the number here: "))

    fab_num = [1, 1]

    for i in range(n):
        if i > 1:
            ith_num = fab_num[i-2] + fab_num[i-1]
            fab_num.append(ith_num)
        # if i == 0 or i == 1:
        #     print("The {0}th fabonacci number is {1}.".format(i+1, fab_num[i]))

    print("The {0}th fabonacci number is {1}.".format(i+1, fab_num[i]))

main()
