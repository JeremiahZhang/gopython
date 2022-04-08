def find_number():
	lst = []
	for i in range(2000, 3201):
		if ((i%7) == 0) & ((i%5) != 0):
			lst.append(str(i))
	num_str = ','.join(lst) # elements in lst must be string
	return(num_str)

def main():
	res = find_number()
	
	print(res)

if __name__ == '__main__':
	main()