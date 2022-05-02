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

# Composite keys

holidays = {
	(1, 1): 'New Years',
	(3, 14): 'Pi day',
	(9, 13): "Programmer's day",
}

print(holidays[3, 14])

# set
tech_stocks1 = {'IBM', 'AAPL', 'MSFT'}
tech_stocks2 = set(['IBN', 'AAPL', 'MSFT'])

print(tech_stocks1)
print(tech_stocks2)

if 'IBM' in tech_stocks1:
	print("Yes, {} in the stocks repository".format('IBM'))

print('FB' in tech_stocks1)

# unique
names = ['IBM', 'AAPL', 'GOOG', 'IBM', 'GOOG', 'YHOO']
unique = set(names)

unique.add('CAT')
unique.add('META')
unique.remove('YHOO')
print(type(unique))