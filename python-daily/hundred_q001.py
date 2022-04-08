def factor(n):
	factor = n
	while n > 1:
		factor = factor * (n-1)
		n -= 1

	return(factor)

def factor_re(n):
	if n == 0:
		return(1)

	return(n * factor_re(n-1))


def main():
	n = int(input('Enter your number:'))
	res = factor(n)
	print(res)
	rel = factor_re(n)
	print('Faster using recrusive function:>', rel)

if __name__ == '__main__':
	main()