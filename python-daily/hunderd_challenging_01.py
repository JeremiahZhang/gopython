def find_number():
	""" 
	Question:
		Write a program which will find all 
		such numbers which are divisible by 7 but 
		are not a multiple of 5,
		between 2000 and 3200 (both included).
		The numbers obtained should be printed 
		in a comma-separated sequence on a single line.
	"""
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