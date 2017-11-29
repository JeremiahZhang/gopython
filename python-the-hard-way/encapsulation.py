# -*- coding: utf-8 -*-

class Encapsulation(object):

	def __init__(self, a, b, c):
		self.public = a
		self._protected = b
		self.__private = c

"""

name  Public    Can be accessed from inside and outside

_name Protected Like a public member, but they shouldnot be directly 
				accessed from outside.

__name Private 	Can't be seen and accessed from outside.

"""