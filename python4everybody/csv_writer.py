import csv

with open('beneficiary.csv', 'w') as new_file:
    new_file_writer = csv.writer(new_file)
    new_file_writer.writerow(['usr_id', 'beneficiary'])
    new_file_writer.writerow([1, 'xyz'])
    new_file_writer.writerow([2, 'pqr'])
    new_file_writer.writerow([3, 'hello'])

with open('beneficiary.csv', 'r') as usr_file:
    usr_file_reader = csv.reader(usr_file)
    for row in usr_file_reader:
        print(row)
