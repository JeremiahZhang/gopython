"""
Print out a list of people 
with same birth year

source:
https://stackoverflow.com/questions/71850828
/print-out-a-list-of-people-with-same-birth-year-in-python
/71850859#71850859

list_1 = ["John", "1991", "male"]
list_2 = ["Mac", "1992", "male"]
list_3 = ["Ria", "1991", "female"]

Born in 1991:
John, male
Ria, female
Born in 1992:
Mac, male
"""

ppl_1 = ["John", "1991", "male"]
ppl_2 = ["Mac", "1992", "male"]
ppl_3 = ["Ria", "1991", "male"]

tmp = {}
for people in (ppl_1, ppl_2, ppl_3):
	name, year, sex = people
	# tmp[year] = (name, sex) cannot store multiple ppls
	tmp.setdefault(year, []).append((name, sex))

print(tmp)

for year in tmp:
	print("Born in {}".format(year))
	for character in tmp[year]:
		print(",".join(character))