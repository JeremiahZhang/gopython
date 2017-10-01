#!/usr/bin/env python3

# avg2.py
#   A simple program to average two exam scores
#   Illustrates use of multiple input

def main():
    print("This program computes two average of two exam scores.")

    score1, score2, score3 = eval(input("Enter three scores separated by a comma: "))
    average = (score1 + score2 + score3) / 3

    print("The average of the scores is: {}".format(average))

main()
