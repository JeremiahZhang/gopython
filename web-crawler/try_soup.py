from bs4 import BeautifulSoup

example_file = open('example.html')
example_soup = BeautifulSoup(example_file.read(), features='lxml')
elems = example_soup.select('#author')
print(type(elems))

print(len(elems))

print(type(elems[0]))

print(elems[0].getText())

# Finding an element with the select() method

p_elems = example_soup.select('p')
print(str(p_elems[0]))
print(p_elems[0].getText())

print(p_elems[1].getText())

print(str(p_elems[2]))

print(p_elems[2].getText())

# Getting data from an element's attributes
span_elem = example_soup.select('span')[0]

print(str(span_elem))
id = span_elem.get('id')
print('Span id:', id)
print(span_elem.get('some_nonexist_addr'))

print(span_elem.attrs)

