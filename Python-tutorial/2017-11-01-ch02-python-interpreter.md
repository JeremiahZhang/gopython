# 2 Python interpreter

> Executable Python Scripts    
> On BSD’ish Unix systems, Python scripts can be made directly executable, like shell scripts, by putting the line.


```
#! /usr/bin/env python
```

Linux 系统上, Python 编译器的安装路径 `/usr/local/bin/python`. 以后我们看到这个, 就不再疑惑.

>  putting `/usr/local/bin` in your Unix shell’s search path makes it possible to start it by typing the command

```
python
```

路径`/usr/local/bin` 放在 Unix shell 的搜索路径上, 这样在命令行下键入`python`可直接启用 Python 编译器. Windows 系统, 请自行查阅处理.

---

启用 Python 编译器方法:

```
python [-bBdEiOQsRStuUvVWxX3?] [-c command | -m module-name | script | - ] [args]
```

常用:

```
python myscript.py
```

---

## 源码编码 Source Code Encoding

> Python source files are treated as encoded in UTF-8. In that encoding, characters of most languages in the world can be used simultaneously in string literals, identifiers and comments — although the standard library only uses ASCII characters for identifiers, a convention that any portable code should follow. To display all these characters properly, your editor must recognize that the file is UTF-8, and it must use a font that supports all the characters in the file.

```
# -*- coding: encoding -*-
```

`encoding` 可改为不同的编码形式, 具体参考[7.8. codecs — Codec registry and base classes — Python 2.7.14 documentation](https://docs.python.org/2.7/library/codecs.html#codec-objects).比如

```
# -*- coding: utf-8 -*-
```

---

```
2017-11-01 v1.0
```