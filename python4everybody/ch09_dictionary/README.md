# Dictionary

再次学习 Python 的 `dictionary`, 突然明白为什么称为字典. 想到以前所用的新华字典, 就是一一对应的关系. {key: value}, 如此理解, 印象深刻.

- 新华`字典`
    - key: 不认识的字
    - value: 该字的意思, 拼音等等
- 字典中 `key-value` 对 顺序不可预测.
- 字典中查阅时都是通过`key`查找, 和现实中使用字典一样.
    - 如果要使用`value`, 则先把`value`提取出来:
        - vals = list(ch2eng_dict.values())

# 1 Pythonic `dict.get()` method
- 刷新Dictionary的使用模式: `get()` method

想看看 dictionary 有哪些 method:

```
>>> dir(dict)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
```

再看看 `get()` method 的 注释: 

```
>>> help(dict.get)
Help on method_descriptor:

get(...)
    D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
```

即:

```
counts = dict()
x = counts.get(name, 0)
```

等价于:

```
if name in counts:
    x = counts[name]
else:
    x = 0
```

WOW, very Pythonic.

## 2 Pythonic Script Counts Words in Text

下面是教材中的案例, 此案例计算了`names`中单词的个数, 如果将`names`变为一个文本, 那么, 我们就可以计算整个文本中单词数目啦.

```
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
```

Pythonic Counting Pattern:

```
counts = dict()
print('Enter a line of text: ')
line = input('')

words = line.split()

print('Words:', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts:', counts)
```

让我们来看一下结果:

```
PS C:\Users\Jeremy\Documents\vocation\gopython\python4everybody\ch09_dictionary> python .\counting_pattern.py
Enter a line of text:
hello your are my cat. My cat is very lovely. I love my cat.
Words: ['hello', 'your', 'are', 'my', 'cat.', 'My', 'cat', 'is', 'very', 'lovely.', 'I', 'love', 'my', 'cat.']
Counting...
Counts: {'hello': 1, 'your': 1, 'are': 1, 'my': 2, 'cat.': 2, 'My': 1, 'cat': 1, 'is': 1, 'very': 1, 'lovely.': 1, 'I': 1, 'love': 1}
```

我们可以发现 

- `cat.` 与 `cat` 分开计算. 在实际中, 我们需要把标点符号要去掉.(教材中也有讲到, 和我不一样的方法)
    - 问题: 一定要去掉标点符号么?
    - 如何去掉标点符号呢?
    - 可参考: [python - Split Strings with Multiple Delimiters? - Stack Overflow](https://stackoverflow.com/questions/1059559/split-strings-with-multiple-delimiters)
- `My` 和 `my` 也是分开计算.
    - 这个可以将所有大写转化为小写就能解决. 

以下修改, 使用正则表达式:

```
import re

counts = dict()
print('Enter a line of text: ')
line = input('')
line = line.lower()

words = re.split(r'\W+', line)

print('Words:', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts:', counts)
```

结果:

```
PS C:\Users\Jeremy\Documents\vocation\gopython\python4everybody\ch09_dictionary> python .\counting_pattern.py
Enter a line of text:
hello your are my cat. My cat is very lovely. I love my cat.
Words: ['hello', 'your', 'are', 'my', 'cat', 'my', 'cat', 'is', 'very', 'lovely', 'i', 'love', 'my', 'cat', '']
Counting...
Counts: {'hello': 1, 'your': 1, 'are': 1, 'my': 3, 'cat': 3, 'is': 1, 'very': 1, 'lovely': 1, 'i': 1, 'love': 1, '': 1}
```

## 3 Loops of Dictionaries

```
In [9]: counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}

In [10]: for key in counts:
    ...:     print(key, counts[key])
    ...:
chuck 1
annie 42
jan 100

In [11]: for key, val in counts:
    ...:     print(key, val)
    ...:
-------------------------------------------------------------------------
ValueError                              Traceback (most recent call last)
<ipython-input-11-ea25e4922583> in <module>()
----> 1 for key, val in counts:
      2     print(key, val)
      3

ValueError: too many values to unpack (expected 2)

In [12]: for (key, val) in counts:
    ...:     print(key, val)
    ...:
-------------------------------------------------------------------------
ValueError                              Traceback (most recent call last)
<ipython-input-12-ef79d0ca5d1d> in <module>()
----> 1 for (key, val) in counts:
      2     print(key, val)
      3

ValueError: too many values to unpack (expected 2)

In [13]: for (key, val) in counts.items():
    ...:     print(key, val)
    ...:
chuck 1
annie 42
jan 100

In [14]: for key, val in counts.items():
    ...:     print(key, val)
    ...:
chuck 1
annie 42
jan 100
```

非常有用的案例, 相对字典的 `key` 排序, 再输出对应 `value`:

```
In [1]: counts = {'chuck': 1, 'fish': 177.5, 'moive': 38}

In [2]: lst = list(counts.keys())

In [3]: print(lst)
['chuck', 'fish', 'moive']

In [4]: counts['breakfast'] = 4

In [5]: print(counts)
{'chuck': 1, 'fish': 177.5, 'moive': 38, 'breakfast': 4}

In [6]: lst = list(counts.keys())

In [7]: print(lst)
['chuck', 'fish', 'moive', 'breakfast']

In [8]: lst.sort()

In [9]: for key in lst:
   ...:     print(key, counts[key])
   ...:
breakfast 4
chuck 1
fish 177.5
moive 38
```

## 4 Retrieving Lists of Keys and Values

## 5 Two Iteration Variables

---

## 教材笔记

- 创建字典, 使用字典
- 字典中 key-value 对 顺序不可预测.
- 字典中查阅时都是通过`key`查找, 和现实中使用字典一样.
    - 如果要使用`value`, 则先把`value`提取出来:
        - vals = list(ch2eng_dict.values())
    - list 和 dict 中 `in` 搜索方式是不一样的.
- 字典的作用
    - Dictionary as a set of counters
    - Dictionaries and files
    - Advanced text parsing

> The in operator uses different algorithms for lists and dictionaries. For lists, it uses a linear search algorithm. As the list gets longer, the search time gets longer in direct proportion to the length of the list. For dictionaries, Python uses an algorithm called a hash table that has a remarkable property: the in operator takes about the same amount of time no matter how many items there are in a dictionary. I won't explain why hash functions are so magical, but you can read more about it at wikipedia.org/wiki/Hash_table.

```
>>> eng2sp = dict()
>>> print(eng2sp)
{}
>>> eng2sp['one'] = 'uno'
>>> print(eng2sp)
{'one': 'uno'}
>>> eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
>>> print(eng2sp)
{'one': 'uno', 'two': 'dos', 'three': 'tres'}
>>> print(eng2sp)
{'one': 'uno', 'two': 'dos', 'three': 'tres'}
>>> print(eng2sp)
{'one': 'uno', 'two': 'dos', 'three': 'tres'}
>>> print(eng2sp)
{'one': 'uno', 'two': 'dos', 'three': 'tres'}
>>> print(eng2sp['two'])
dos
>>> eng2sp['four'] = 'for'
>>> print(eng2sp)
{'one': 'uno', 'two': 'dos', 'three': 'tres', 'four': 'for'}
>>> print(eng2sp['five'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'five'
>>> len(eng2sp)
4
>>> 'one' in eng2sp
True
>>> 'uno' in eng2sp
False
>>> vals = list(eng2sp.values())
>>> 'uno' in vals
True
```

- Dictionary as a set of counters

```
In [1]: word = 'brontosaurus'

In [2]: d = dict()

In [3]: for c in word:
   ...:     if c not in d:
   ...:         d[c] = 1
   ...:     else:
   ...:         d[c] += 1
   ...:

In [4]: print(d)
{'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}
```

- `get` method of dictionaries

```
In [5]: counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}

In [6]: print(counts.get('jan', 0))
100

In [7]: print(counts.get('tim', 0))
0

In [8]: print(counts)
{'chuck': 1, 'annie': 42, 'jan': 100}
```

## 高级文本分析, 标点及大小写

```
In [10]: import string

In [11]: string.punctuation
Out[11]: '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
```

案例:

```
import string

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

fhand.close()

print(counts)
```
