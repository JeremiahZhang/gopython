class SchoolMember:
	"""Represents any school member"""

	def __init__(self, name, age):
		super(SchoolMember, self).__init__()
		self.name = name
		self.age = age
		print('(Initialized SchoolMember: {})'.format(self.name))

	def tell(self):
		'''Tell my details.'''
		print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
	"""Represents a Teacher"""
	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)
		self.salary = salary
		print('(Initialized Teacher: {})'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
	"""Represents a Student"""
	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print('(Initialized Student: {})'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Marks: "{:d}"'.format(self.marks))

lei = Teacher('Mr. Zhang', 25, 30000)
ch = Student('Shen Chen', 18, 80)

print()

members = [lei, ch]
for member in members:
	member.tell()
		
		