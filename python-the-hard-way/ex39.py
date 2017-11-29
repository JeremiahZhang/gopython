# -*- coding: utf-8 -*-

# Dictionaries

"""
Dictionaries store connections between pieces of 
information. Each item in a dictionary is a key-value pair.
"""

# creat a simple dictionary
alien = {'color': 'red', 'points': 5}

# Accessing a value
print "The alien's color is", alien['color']

# Adding a new key-value pair
alien['x_postion'] = 0

# Looping through all key-value pairs
fav_number = {'eric': 17, 'ever': 4}
for name, number in fav_number.items():
	print name + " loves " + str(number)

# looping through all keys
for name in fav_number.keys():
	print name, "loves a number"

# Looping through all values
for number in fav_number.values():
	print str(number), "is a favorite."

# A dictionary example

# creat a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

# creat a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# add some more citites
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY state has: ", cities['NY']
print "OR state has: ", cities['OR']

# print some states
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then citites dict
print "-" * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print "-" * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print "-" * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print "-" * 10
for state, abbrev in states.items():
	print "%s state is abbrevitated %s and has city %s" % \
		(state, abbrev, cities[abbrev])

print "-" * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
	print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city

# del dictionary elements
print "The cities['NY'] is", cities['NY']
del cities['NY']
city = cities.get('NY')
if not city:
	print "Sorry, NY has been deleted."