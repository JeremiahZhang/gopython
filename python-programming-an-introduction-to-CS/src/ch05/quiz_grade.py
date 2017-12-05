# quiz_grade.py
#   Exercises 2 in chapter 5
#   A program to accept a quiz score as an input and
#   print out the corresponding grade.

def main():
    print("This program is to convert quiz score to gradde.")

    # Get the quiz score.
    score = eval(input("Please enter a quiz score (0-5): "))

    # Convert
    grades = ["A", "B", "C", "D", "E", "F"]
    grade = grades[5 - score]

    # Output
    print("The grade of score {0} is {1}.".format(score, grade))

if __name__ == '__main__':
    main()
