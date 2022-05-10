animals = ['Python', 'Viper', 'Cobra']

def add_snake(snake_type):
	animals.extend(snake_type)
	print(animals)

add_snake('Boa')