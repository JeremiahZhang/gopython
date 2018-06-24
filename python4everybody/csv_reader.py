import csv

with open('beneficiary.csv', 'r') as user_file:
    user_file_reader = csv.reader(user_file)
    for row in user_file_reader:
        print(row)
