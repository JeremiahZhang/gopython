# sum_numbers.py
#   A program to sum a series of numbers entered by the usr.
#   The program first prompts the usr for how many numbers are
#   to be summed.
#   Then, it imput each of the numbers, and print a total sum.

def main():
    n = eval(input("How many numbers do you want to sum? Enter: "))

    sum = 0

    for i in range(n):
        print("Please enter the {} number: ".format(i+1))
        num = eval(input())

        sum += num

    avg = sum / n

    print("The sum of {0} numbers is {1}.".format(n, sum))
    print("The average is {}.".format(avg))

main()
