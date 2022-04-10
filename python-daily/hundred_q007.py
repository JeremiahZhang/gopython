def sort_input(s):
	str_lst = s.split(",")
	str_lst.sort()
	print(','.join(str_lst))


def main():
	s = input("Separted by comma >>>")
	sort_input(s)

if __name__ == '__main__':
	main()