# -*- coding: utf-8 -*-

# make a list
bikes = ['trek', 'mereda', 'giant']

# get the first item in a list
first_bike = bikes[0]
print "The first bike is %s." % first_bike

# get the last item in a list
last_bike = bikes[-1]
print "The last bike is", last_bike

# looping through a list
for bike in bikes:
	print(bike)

# adding items to a list
bikes = []
bikes.append('mereda')
bikes.append('giant')
bikes.append('trek')
bikes.append('fenghuan')

print "Then the first bike is", bikes[0]

# making numerical lists
squares = []

for x in range(1, 11):
	squares.append(x**2)

print "The first item in list squares is", squares[0]

# list comprehension list 推导式
squares_2 = [x**3 for x in range(1, 3)]

print "The last item in list squares_2 is", squares_2[-1]

# slicing a list
nba_star = ['cobe', 'jeremy', 'james', 'weide']
first_two = nba_star[:2]

print first_two

# copying a list
copy_of_bikes = bikes[:]
print copy_of_bikes

# ex38

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are note 10 things in that list. Let's fix that."

stuff = ten_things.split(' ') # list

print type(stuff)

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", \
			"Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print " ".join(stuff) # list to string
print "#".join(stuff[3:5]) # list to string


"""

# lists are one of the most common data structures 
# programmers use

 Every concept in programming usually has 
 some relationship to the real world. 
 """