def to_binary(num):
	if num == 0:
		return(1)

	if num > 1:
		to_binary(num // 2)


	# remainder
	print(num % 2)

def main():
	n = int(input())
	to_binary(n)

if __name__ == '__main__':
	main()