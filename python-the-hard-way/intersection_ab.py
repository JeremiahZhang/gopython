x_2 = []
x_3 = []

for i in range(0, 11):
	x_2.append(i**2)

print x_2

for i in range(0, 11):
	x_3.append(i**3)

print x_3

for i in range(0, 11):
	if x_2[i] == x_3[i]:
		print i
	else:
		print "there is not equal number."