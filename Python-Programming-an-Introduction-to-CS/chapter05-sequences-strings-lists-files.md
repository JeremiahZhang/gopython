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
