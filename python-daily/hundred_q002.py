def answer(n):
	"""Generate a diction that contain(i, i**2)"""
	res = {}
	for i in range(1, n+1):
		res[i] = i ** 2

	return(res)

def main():
	n = int(input('Give an integer(>0): '))
	res = answer(n)
	print(res)


if __name__ == '__main__':
	main()