# 与非
def and_not(a, b):
	return(not (a and b))

# 或非
def or_not(a, b):
	return(not (a or b))

# 与或非
def and_or_not(a,b,c,d):
	return(not ((a and b) or (c and d)))

# 异或
def yi_or(a, b):
	return((a and (not b)) or ((not a) & b))

# 同或
def tong_or(a, b):
	return((a and b) or ((not a) and (not b)))

def main():
	print(and_not(0, 0))

if __name__ == '__main__':
	main()