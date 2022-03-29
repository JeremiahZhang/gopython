"""
There are 5 students in this class whose names and grades 
are assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], 
                   ['Tina', 37.2], ['Akriti', 41], 
                   ['Harsh', 39]]

The lowest grade 37.2 of belongs to Tina. The second lowest 
grade of belongs to both Harry and Berry, so we order 
their names *alphabetically* and *print* each name on a new line.

input:
	5
	Harry
	37.21
	Berry
	37.21
	Tina
	37.2
	Akriti
	41
	Harsh
	39

output:
	Berry
	Harry
"""

if __name__ == '__main__':
    records = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        student = [name, score]
        records.append(student)
        # print(records)
    
    scores = [x[1] for x in records]
    # print(scores)
    lst_scores = list(set(scores))
    lst_scores.sort()
    # print(lst_scores)
    sceond_lowest_score = lst_scores[1]
    
    second_lowest_stu = [x[0] for x in records if x[1] == sceond_lowest_score]
    second_lowest_stu.sort()
    for student in second_lowest_stu:
        print(student)