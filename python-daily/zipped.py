columns = ['name', 'shares', 'price']
values = ['GOOG', 100, 490.12]

pairs = zip(columns, values)

print(type(pairs))

for name, value in pairs:
	print(name,value)