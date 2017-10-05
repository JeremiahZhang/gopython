# 第五章-Sequences: strings, lists, files.

- 目标
    - **String data type**, how they are represented in the computer.
    - **Operations can be performed on strings**
        - Built-in functions
        - String methods
    - **Basic idea of sequences and indexing** as they apply on Python strings and lists.
    - Apply **string formatting** to produce attractive, informative program output.
    - **Basic file processing concepts and techniques** for reading and writing text files in Python.
    - **Basic concepts of cryptography**(密码学).
    - Understand and write programs that **process textual information**.
- Sum

---

## 1.The String Data Type

> You can think of a string as a sequence of characters.

### 1.1 String Basic

input - variable - ouput:

```
anifacc@mint /media/anifacc/geek/gopython/Python-Programming-an-Introduction-to-CS/src/ch05 $ python3
Python 3.5.2 (default, Sep 14 2017, 22:51:06)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> str1 = "hello"
>>> str2 = 'spam'
>>> print(str1, str2)
hello spam
>>> type(str1)
<class 'str'>
>>> type(str2)
<class 'str'>
>>> first_name = input("Pleae enter your name:")
Pleae enter your name:Jeremy
>>> print("Hello", first_name)
Hello Jeremy
>>>
```

### 1.2 String Operations

Python 中 index 开始的是 0. String 也可是使用 index 获取相关 characters.

> 1 Operation: index

```
>>> greet = "Hello Jeremy"
>>> greet[0]
'H'
>>> print(greet[0], greet[2], greet[4])
H l o
>>> x = 8
>>> print(greet[x-2])
J
>>> greet[-1]
'y'
>>> greet[-2]
'm'
>>> greet[-3]
'e'
>>> greet[-4]
'r'
>>> greet[-5]
'e'
>>> greet[-6]
'J'
>>>
```

> 2 Operation, slice 切片形式:

```
>>> greet[0: 3]
'Hel'
>>> greet[5: 9]
' Jer'
>>> greet[:5]
'Hello'
>>> greet[5:]
' Jeremy'
>>> greet[:]
'Hello Jeremy'
```

> Sum: Python string Operation.

| Operation             | Meaning     |
| :-------------        | :------------- |
| `+`                   | Concatenation 串联一起        |
| `*`                   | Repetition 复制,重复          |
| <string>[]            | Indexing 索引                |
| <string>[ : ]         | Slicing 切片                |
| len(<string>)         | Length  长度                |
| for <var> in <string>:| Iteration through characters |

`+` 将 两 strings `粘贴` 连接起来.

```
>>> "spam" + "eggs"
'spameggs'
>>> "Spam" + "And" + "Eggs"
'SpamAndEggs'
>>> 3 * spam
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> 3 * "spam"
'spamspamspam'
>>> "spam" * 5
'spamspamspamspamspam'
>>> (3 * "spam") + ("Eggs" * 5)
'spamspamspamEggsEggsEggsEggsEggs'
>>> len("spam")
4
>>> len("SpamAndEggs")
11
>>> for ch in "Spam!":
...     print(ch, end=" ")
...
S p a m !
>>>
```

---

## 2.字符串处理: Simple String Processing

Username and password combination:

> One scheme for generating usernames is to use the user's first initial followed by up to seven letters of the user's last name.

Example:

- `Elmer Thudpucker -- > ethudpuc`
- `John Smith --> jsmith`

---

## 3.Lists as Sequences

> Python lists are also a kind of Sequences.

因此, String 中 的 operation , 同样适用于 List.

```
S/src/ch05 $ python3
Python 3.5.2 (default, Sep 14 2017, 22:51:06)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> [1, 2] + [3, 4]
[1, 2, 3, 4]
>>> [1, 2] * 3
[1, 2, 1, 2, 1, 2]
>>> grades = ['a', 'b', 'c', 'd', 'e']
>>> grades[0]
'a'
>>> grades[2: 4]
['c', 'd']
>>> len(grades)
5
```

> Lists can be sequences of arbitrary objects.

List 的厉害之处就是可以存放 任意类型的数据, 对象.

```
>>> my_list = [1, 'Spam', 4, 'U']
>>> my_list
[1, 'Spam', 4, 'U']
```

> Lists are mutable. Strings are not.

```
05 $ python3
Python 3.5.2 (default, Sep 14 2017, 22:51:06)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> my_list = [1, 3, 5, 7]
>>> my_list[2]
5
>>> my_list[2] = 9
>>> my_list
[1, 3, 9, 7]
>>>
>>> my_string = 'Hello World'
>>> my_string[2]
'l'
>>> my_string[2] = 'Z'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

---

## 4.String Representation and Message Encoding

### 4.1 String Representation

String 表达, 计算机的执行 与 数值执行 没有任何差异. 只不过是 String 而已.

类比:

- 编码: 课堂传纸条, 使用密码:
    - `a-z: 1-26`
    - `18, 14, 20, 17, 15, 20, 18, 18` represents a word.
    - 这类似 计算机表示 strings 的方法.

> Each character is translated into a number, and the entire string is stored as a sequence of (binary) numbers in computer memory. It doesn't really matter what number is used to represent any given character as long as the computer is consistent about the encoding/decoding process.

> In the early days of computing, different designers and manufacturers used different encodings. You can imagine what a headache this was for people transferring data between different systems.

现在有标准啦: industry standard encodings.

- **ASCII**(American Standard Code for Information Interchange) 0-127 to represent the characters typically found on an (American) computer keyboard, as well as certain special values known as *control codes* that are used to coordinate the sending and receiving of Information.
    - 大写 `A-Z : 65-90`
    - 小写 `a-z : 97-122`
    - problem: it is American-centric. It doesnot have symbols that are needed in many other languages.
    - Extended ASCII encodings. Unicode.
- `Unicode`: a much larger standard that includes support for the characters of nearly all written languages.
    - *Python strings support the Unicode standard*, so you can wrangle characters from just about any language, provided your os has appropriate fonts for displaying the characters.
    - *Built-in funcitions*:
        - `ord`: returns the numeric("ordinal") code of a single-character string.
        - `chr`: gees the other direction.

```
>>> ord('a')
97
>>> ord('A')
65
>>> chr(97)
'a'
>>> chr(90)
'Z'
```

上面的编码是按 ASCII 标准执行的诺.

- The addressable piece is typically 8 bits = 1 byte of memory.
- 1 byte = 2 ^ 8 = 256 bits, 可存 256种 different values

这样看, ASCII 编码 使用 7bits = 2^7 = 128. 而在 Unicode 总, 1 byte 不能满足存储 100,000+ 可能的 Unicode 编码 字符 characters. 怎么办呢?  **UTF-8**.

- `UTF-8` encoding:
    - A variable-length encoding that uses a single byte to store characters that are in the ASCII subset, but may need up to 4 bytes in order to represent some of the more esoteric characters.
    - That means that a string of length 10 characters will end up getting stored in memory as a sequence between 10 and 40 bytes, depending on the actual characters used in the string.

### 4.2 Programming an Encoder

`text2numbers.py`

---

## 5.String Methods

### 5.1 Programming a Decoder.

`分割string: string.split(<params>)`

```
>>> my_string = 'hello, string methods!'
>>> my_string.split()
['hello,', 'string', 'methods!']
>>> "32,24,25,57".split(",")
['32', '24', '25', '57']
>>> "1, 3, 5, 57".split(", ")
['1', '3', '5', '57']
>>> "1, 3, 5, 57".split(",")
['1', ' 3', ' 5', ' 57']
>>>
```

`.split()` 中的参数不同, 结果也不同. 输出的结果是 `list`, a list of strings.

```
>>> num_str = '500'
>>> a = eval(num_str)
>>> a
500
>>> type(a)
<class 'int'>
>>> eval('345.67')
345.67
>>> x = 3.5
>>> y = 4.7
>>> eval(x * y)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: eval() arg 1 must be a string, bytes or code object
>>> eval('x * y')
16.45
>>> x = eval(input('Enter a number: '))
Enter a number: 3.14
>>> print x
  File "<stdin>", line 1
    print x
          ^
SyntaxError: Missing parentheses in call to 'print'
>>> print(x)
3.14
```

### 5.2 More String methods

```
>>> s = 'hello, I came here for an argument'
>>> s.captitalize()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'captitalize'
>>> s.capitalize()
'Hello, i came here for an argument'
>>> s.title()
'Hello, I Came Here For An Argument'
>>> s.lower()
'hello, i came here for an argument'
>>> s.upper()
'HELLO, I CAME HERE FOR AN ARGUMENT'
>>> s
'hello, I came here for an argument'
>>> s.replace('I', 'you')
'hello, you came here for an argument'
>>> s.center(30)
'hello, I came here for an argument'
>>> s.center(50)
'        hello, I came here for an argument        '
>>> s.count('e')
5
>>> s.find(',')
5
>>> " ".join(['Number', 'one,', 'the', 'Larch'])
'Number one, the Larch'
>>> 'spam '.join(['Number', 'one,', 'the', 'Larch'])
'Numberspam one,spam thespam Larch'
>>>

>>> ss = " hello "
>>> ss.lstrip()
'hello '
>>> ss.rstrip()
' hello'
>>>

```

- `s.capitalize()`: Copy of s with only the 1st character capitalized
- `s.center(width)`: Copy of s Centered s in a filed of given width
- `s.count(sub)`: Find the number of occurrence of sub in `s`
- `s.find(sub)`: Find the 1st position where `sub` occurs in `s`
- `s.join(list)`: Concatenate `list` into a string, using `s` as separator
- `s.ljust(width)`: Like `center`, but s is left-justified.
- `s.lower()`
- `s.lstrip()`: Copy of `s` with leading white space removed.
- `s.replace(old_sub, new_sub)`
- `s.rfind(sub)`: Like `find`, but returns the rightmost position
- `s.rjust(width)`: Like `center`, but `s` is right-justified.
- `s.rstrip()`: Copy of `s` with trailing white space removed.
- `s.split()`: Split `s` into a list  of substrings
- `s.title()`: Copy of `s` with first character of each word capitalized
- `s.upper()`: Copy of `s` with all characters converted to upper case.

---

## 6.List Methods

`list.append()`

and so on, 详细查看 python document

---

## 7.From Encoding to Encryption

> The process of Encoding information for the purpose of keeping it secret or transmitting it privately is called *Encryption*.

- Encryption
    - `plaintext` 明码
    - `cipher alphabet` 编码表
    - `ciphertext` 密码
- private key
- public key

---


---

## Sum
