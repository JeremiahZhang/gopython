"""
Find the difference between two lists or sets

Input:
solution.solution([13, 5, 6, 2, 5], [5, 2, 5, 13])
Output:
    6

Input:
solution.solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50])
Output:
    -4

-- Java cases --
Input:
Solution.solution({13, 5, 6, 2, 5}, {5, 2, 5, 13})
Output:
    6

Input:
Solution.solution({14, 27, 1, 4, 2, 50, 3, 1}, {2, 4, -4, 3, 1, 1, 14, 27, 50})
Output:
    -4
"""

def diff_lst_set(x, y):
	x = set(x)
	y = set(y)

	result = x ^ y
	return(list(result))

def main():
	x1 = [13, 5, 6, 2, 5]
	y1 = [5, 2, 5, 13]
	x2 = [14, 27, 1, 4, 2, 50, 3, 1]
	y2 = [2, 4, -4, 3, 1, 1, 14, 27, 50]

	diff1 = diff_lst_set(x1, y1)
	diff2 = diff_lst_set(x2, y2)

	print(diff1[0])
	print(diff2[0])



if __name__ == '__main__':
	main()