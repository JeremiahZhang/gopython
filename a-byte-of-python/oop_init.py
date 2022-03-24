class Person:
	"""docstring for Person"""
	def __init__(self, name):
		self.name = name

	def say_hi(self):
		print('Halo, my name is', self.name)

p = Person('Jeremy')
p.say_hi()