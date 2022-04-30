# list as container

portfolio = [
	('GOOG', 100, 490.1),
	('IBM', 50, 91.3),
	('CAT', 150, 83.44)
]

print(portfolio[0])
print(portfolio[2])

# Dicts as a container

prices = {
	'goog': 510.21,
	'cat': 87.21,
	'ibm': 92.12,
	'msft': 44.21
}

print("price of ibm is {}".format(prices['ibm']))