# gpa.py
#   A program to find student with highest GPA
"""
Enter name of the grade file: info_st.md
Susan B, 100, 400

Dibble C, 18, 41.5

The best student is: Susan B
hours: 100.0
GPA: 4.0
"""

class Student:

    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def get_name(self):
        return self.name

    def get_hours(self):
        return self.hours

    def get_qpoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints / self.hours

def make_student(info_str):
    # infor_str is a ", "  line: name hours qpoints
    # return a corresponding Student object.

    name, hours, qpoints = info_str.split(", ")
    return Student(name, hours, qpoints)

def main():
    # open the input file for reading
    file_name = input("Enter name of the grade file: ")
    infile = open(file_name, "r")
    # set best to the record for the first student in the file
    best = make_student(infile.readline())

    # process subsequent lines of the file
    for line in infile:
        # turn the line into a student record
        print(line)
        s = make_student(line)
        # if this student is best so far, remember it.
        if s.gpa() > best.gpa():
            best = s

    infile.close()

    # print information about the best student
    print("The best student is: {}".format(best.get_name()))
    print("hours: {}".format(best.get_hours()))
    print("GPA: {}".format(best.gpa()))

if __name__ == '__main__':
    main()
