# quiz_grade2.py
#   A program to convert 0-100 exam score to the corresponding
#   grade.
#   90-100: A
#   80-89:  B
#   70-79:  C
#   60-69:  D
#   <60:    E

def main():
    print("This program is to convert 0-100 score to grade.")

    # Input
    score = eval(input("Please enter the socre(0-100): "))

    # Convert
    grades = ["A", "B", "C", "D", "E"]
    if score == 100:
        grade = grades[0]
    elif score < 60:
        grade = grades[4]
    else:
        score_grade_relation = (score - 60) // 10 + 1
        print(score_grade_relation)
        grade = grades[4 - score_grade_relation]

    # Output
    print("The grade of the score {0} is {1}".format(score, grade))

if __name__ == '__main__':
    main()
