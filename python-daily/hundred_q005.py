import math

def cal():
	C = 50
	H = 30
	seq = input("Enter your number separated by comma:")
	lst = seq.split(",")
	return([int(math.sqrt(2*C*int(x)/H)) for x in lst])

def main():
	res = cal()
	print(res)

if __name__ == '__main__':
	main()
