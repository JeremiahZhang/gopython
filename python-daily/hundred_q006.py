def generate_array():
	s = input("Enter your 2 numbers separated by ,:")
	lst = s.split(",")
	row, column = int(lst[0]), int(lst[1])
	lst = []
	i = 0

	while i < row:
		lst_row = []
		for j in range(column):
			lst_row.append(i * j)
		i += 1
		lst.append(lst_row)
	return(lst)

def simplify_gen():
	s = input("2 numbers separated by,>>>")
	dims = [int(x) for x in s.split(",")]
	num_row, num_col = dims[0], dims[1]
	# Initialize i x j  2 dimensional list
	multi_lst = [[0 for col in range(num_col)] for row in range(num_row)]

	for i in range(num_row):
		for j in range(num_col):
			multi_lst[i][j] = i * j

	return(multi_lst)

def main():
	res = generate_array()
	print(res)
	print("simplify_gen")
	res = simplify_gen()
	print(res)

if __name__ == '__main__':
	main()