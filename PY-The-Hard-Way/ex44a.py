# -*- coding: utf-8 -*-

class Parent(object):

	def implicit(self):
		print "PARENT implicit()"

class Child(Parent):
	pass

dad = Parent() # create an instance of a class
son = Child() # an instance of a class

dad.implicit() # Parent.implicit()
son.implicit() # Parent.implicit() 儿子继承了父亲的 implicit 函数