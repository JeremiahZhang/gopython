# -*- coding: utf-8 -*-

"""
1. what is a class?
2. whst is an object?
3. what's the difference?
"""

## Animal is-a object (yes, sort of confusing) look at the extra credit.
class Animal(object):
	pass

## Dog is-an animal
class Dog(Animal):

	def __init__(self, name):
		## Dog has-a name
		self.name = name

## The Cat is-an animal
class Cat(Animal):

	def __init__(self, name):
		## the Cat has-a name
		self.name = name

## Person is-a object
class Person(object):

	def __init__(self, name):
		## Person has-a name
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Employee is-a person
class Employee(Person):

	def __init__(self, name, salary):
		## Employee has-a name from the object Person
		## hmm what is thsi strange magic?
		super(Employee, self).__init__(name)
		## Employee has-a salary
		self.salary = salary

## Fish is-an object
class Fish(object):

	def __init__(self, name):
		self.name = name

## Salmon is-a Fish
class Salmon(Fish):
	def __init__(self, name, nose_size):
		super(Salmon, self).__init__(name)

		self.nose_size = nose_size

## Halibut is-a Fish
class Halibut(Fish):
	def __init__(self, name, fins):
		super(Halibut, self).__init__(name)

		self.fins = fins

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet named Satan
mary.pet = satan

## Frank is-a Person, also is-an Employee
## Frank has-a name Frank, and has-a salary 120000
frank = Employee("Frank", 120000)
print "Instance of class Employee(Person)"
print frank # is an object

## Frank has-a pet name Rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish("Hai-Tun")
print "Instanc of class Fish(object)"
print flipper

## crouse is-a Salmon
crouse = Salmon("Crouse", "Long")
print crouse.nose_size

## harry is-a Halibut
harry = Halibut("Harry", "Has fins")
print harry.fins