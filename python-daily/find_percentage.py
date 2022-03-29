if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    query_scores = student_marks[query_name]
    query_avg = sum(query_scores) / len(query_scores)
    
    print("{:0.2f}".format(query_avg))

"""
input:
    2
    Harsh 25 26.5 28
    Anurag 26 28 30
    Harsh
output:
    26.50 # average of his scores.
"""