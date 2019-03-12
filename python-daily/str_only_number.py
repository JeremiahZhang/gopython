# Only keep numbers in a string

string = 'ahfdl123456'
print('The original string is "%s"' % (string))
str_only_num = ''.join(c for c in string if c.isdigit())
num_from_str = int(str_only_num)

print("The output: %d " % (num_from_str))
