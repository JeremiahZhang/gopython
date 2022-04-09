def answer(sequence):
	""" Answer of the Q4
	
	1. Accept a sequence of comma-separated numbers from console
	2. Generate a list and a tuple which contains every number.
	"""
	lst = sequence.split(',')
	tpl = tuple(lst)
	return(lst, tpl)


def main():
	my_input = input('Enter the numbers separated by a comma:> ')
	my_list, my_tuple = answer(my_input)
	print(my_list)
	print(my_tuple)

if __name__ == '__main__':
	main()