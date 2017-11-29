# -*- coding: utf-8 -*-

class Parent(object):

	def override(self):
		print "PARENT override()"

class Child(Parent):
	
	def override(self):
		print "CHILD override()"

dad = Parent() # create an instance of a class
son = Child() # an instance of a class

dad.override() # 父亲的 override() 函数
son.override() # 儿子使用自己class下定义的函数 override() 虽然父亲也有, 但被儿子的覆盖了