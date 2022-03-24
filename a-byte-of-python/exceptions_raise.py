class ShortInputException(Exception):
	"""A user-defined exception class: ShortInputException"""
	def __init__(self, length, atleast):
		super(ShortInputException, self).__init__()
		self.length = length
		self.atleast = atleast

try:
	text = input('Enter something __> ')
	if len(text) < 3:
		raise ShortInputException(len(text), 3)
	# Other work can continue
except EOFError:
	print('Why did you do an EOF on me?')
except ShortInputException as ex:
	print(('ShortInputException: The input was ' +
		   '{0} long, expected at least {1}')
	       .format(ex.length, ex.atleast))
else:
	print('No exception was raised.')
		