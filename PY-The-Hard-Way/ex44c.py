# -*- coding: utf-8 -*-

class Parent(object):

	def altered(self):
		print "PARENT altered()"

class Child(Parent):

	def altered(self):
		print "CHILD, before parent altered()"
		super(Child, self).altered()
		print "CHILD, after parent altered()"

dad = Parent()
son = Child()

dad.altered() # 类（父亲）altered() function
son.altered() # 类（儿子）子类的 altered() funciton 后 super 父类 的 altered() function