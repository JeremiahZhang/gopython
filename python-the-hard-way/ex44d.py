# -*- coding: utf-8 -*-

class Parent(object):

	def override(self):
		print "Parent override()"

	def implicit(self):
		print "Parent implicit()"

	def altered(self):
		print "PARENT altered()"

class Child(Parent):

	def override(self):
		print "Child override()"

	def altered(self):
		print "CHILD, before parent altered()"
		super(Child, self).altered()
		print "CHILD, after parent altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered() # 类（父亲）altered() function
son.altered() # 类（儿子）子类的 altered() funciton 后 super 父类 的 altered() function