# level 1
# http://www.pythonchallenge.com/pc/def/map.html
import string

def solution(my_string):
	text = ""
	for char in my_string:
		if char.isalpha():
			if char == "y":
				decrypt_char = "a"
			elif char == "z":
				decrypt_char = "b"
			elif char == "Y":
				decrypt_char = "A"
			elif char == "Z":
				decrypt_char = "B"
			else:
				decrypt_char = chr(ord(char) + 2)
			
			text = text + decrypt_char
		else:
			text = text + char

	return text

def solution_trans(my_string):
	x = string.ascii_lowercase + string.ascii_uppercase
	y = string.ascii_lowercase[2:] + string.ascii_lowercase[:2] \
	    + string.ascii_uppercase[2:] + string.ascii_uppercase[:2]
	mytable = my_string.maketrans(x, y)
	return(my_string.translate(mytable))


def main():
	my_string = input('Enter:>')
	#decrypt_string = solution(my_string)
	decrypt_string = solution_trans(my_string)
	print(decrypt_string)

if __name__ == '__main__':
	main()