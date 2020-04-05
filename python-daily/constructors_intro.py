# constuctors and special methods

## example

class Apple:
	def __init__(self, color, flavor): # construcotrs
		self.color = color
		self.flavor = flavor
	def __str__(self):
		return "This apple is {} and its flavor is {}".format(self.color, self.flavor)

jonagold = Apple("red", "sweet")
print(jonagold.color)
print(jonagold)

## exercise 

class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is {}".format(self.name)

# Create a new instance with a name of your choice
some_person = Person("David") 
# Call the greeting method
print(some_person.greeting())