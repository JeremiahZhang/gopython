class InOutString:
	"""Class has get_string and print_string method."""

	def __init__(self):
		self.input_str = ""
		
	def get_string(self):
		self.input_str = input("Enter your string ::>")

	def print_string(self):
		print(self.input_str.upper())

def main():
	MyClassObj = InOutString()
	MyClassObj.get_string()
	MyClassObj.print_string()
	

if __name__ == '__main__':
	main()