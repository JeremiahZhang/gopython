import string

def reverse(text):
	return text[::-1]


# 判断是否是回文 palindrome
def is_palindrome(text):
	return text == reverse(text)


something = input("Enter text: ")
sth_without_space = something.replace(' ', '')
print('Something without whitespace', sth_without_space)

new_sth = sth_without_space.translate(str.maketrans('', '', string.punctuation))
print('Something remove punctuations', new_sth)

if is_palindrome(new_sth):
	print('Yes, it is a palindrome')
else:
	print('No, it is not a palindrome')