# -*- coding: utf-8 -*-

class Other(object):

	def override(self):
		print "Other override()"

	def implicit(self):
		print "Other implicit()"

	def altered(self):
		print "Other altered()"

class Child(object):

	def  __init__(self):
		self.other = Other() # 主要是这里 create an instance of a class Other

	def implicit(self):
		self.other.implicit()

	def override(self):
		print "CHILD override()"

	def altered(self):
		print "CHILD, before Other altered()"
		self.other.altered()
		print "CHILD, AFTER Other altered()"

son = Child() # an instance of a class named Child

son.implicit()
son.override()
son.altered()