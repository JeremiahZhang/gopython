# bs4 note

```
>>> res = requests.get('https://www.douban.com/')
>>> res.raise_for_status()
>>> no_douban_soup = bs4.BeautifulSoup(res.text)

D:\ProgramData\Anaconda2\envs\ten_years\lib\site-packages\bs4\__init__.py:181: UserWarning: No parser was explicitly specified, so I'm using the best
available HTML parser for this system ("html.parser"). This usually isn't a problem, but if you run this code on another system, or in a different vir
tual environment, it may use a different parser and behave differently.

The code that caused this warning is on line 1 of the file <stdin>. To get rid of this warning, change code that looks like this:

 BeautifulSoup(YOUR_MARKUP})

to this:

 BeautifulSoup(YOUR_MARKUP, "html.parser")

  markup_type=markup_type))
  
>>> type(no_douban_soup)

<class 'bs4.BeautifulSoup'>

>>> example_file = open('example.html')

>>> example_soup = bs4.BeautifulSoup(example_file)

>>> type(example_soup)
<class 'bs4.BeautifulSoup'>

>>> elems = example_soup.select('#author')

>>> type(elems)
<class 'list'>

>>> len(elems)
1

>>> type(elems[0])
<class 'bs4.element.Tag'>

>>> str(elems[0])
'<span id="author">Al Sweigart</span>'

>>> elems[0].attrs
{'id': 'author'}

>>> elems[0].getText()
'Al Sweigart'

>>> p_elems = example_soup.select('p')
>>> type(p_elems)
<class 'list'>
>>> len(p_elems)
3
>>> str(p_elems[0])
'<p>Download my <strong>Python</strong> book from <a href="http://\ninventwithpython.com">my website</a>.</p>'

>>> p_elems[0].getText()
'Download my Python book from my website.'

>>> str(p_elems[1])
'<p class="slogan">Learn Python the easy way!</p>'

>>> p_elems[1].getText()
'Learn Python the easy way!'

>>> str(p_elems[2])
'<p>By <span id="author">Al Sweigart</span></p>'

>>> p_elems[2].getText()
'By Al Sweigart'

```

- `soup.select()`: 选择元素
- `soup.get()` 获取元素

```
>>> span_elem = example_soup.select('span')[0]
>>> str(span_elem)
'<span id="author">Al Sweigart</span>'
>>> span_elem.get('id')
'author'
>>> span_elem.get('some_nonexistent_addr') == None
True
>>> span_elem.attrs
{'id': 'author'}
>>>
```