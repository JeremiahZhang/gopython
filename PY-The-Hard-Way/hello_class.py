class Greeting(object):
	def __init__(self, name):
		self.name = name

	def __del__(self):
		print "Destructor started"

	def SayHello(self):
		print "Hello", self.name