import sys
sys.path.append('..')

from ch10.gpa import Student
from ch10.gpa import make_student

def read_students(file_name):
    infile = open(file_name, 'r')
    students = []

    for line in infile:
        students.append(make_student(line)) # A class instance in students

    infile.close()
    return students

def write_students(students, file_name):
    outfile = open(file_name, 'w')
    for s in students:
        print("{0}, {1}, {2}".format(s.get_name(), s.get_hours(), s.get_qpoints()), file=outfile)

    outfile.close()

def main():
    print("This program sorts student grade inform by GPA")
    file_name = input("Enter the name of the data file: ")
    data = read_students(file_name)
    data.sort(key=Student.gpa)
    file_name = input("Enter a name for the output file: ")
    write_students(data, file_name)
    print("The data has been written to {}".format(file_name))

if __name__ == '__main__':
    main()
