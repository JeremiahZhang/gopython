# 代码风格

积累, 规范代码风格

- string 字符串
- naming 命名
- imports formatting: import 格式

---

## 1.String 字符串

(1) 全程使用 `format` or `%` 来 formatting strings.

```
Yes: x = a + b
     x = '%s, %s!' % (imperative, expletive)
     x = '{}, {}!'.format(imperative, expletive)
     x = 'name: %s; score: %d' % (name, n)
     x = 'name: {}; score: {}'.format(name, n)
```

(2) `""` 和 `''` 的使用, 选择了一种, 就确定一种, 保持一致. 不要一会 `""`, 一会又`''`.

```
Yes:
    Python('Why are you hiding your eyes?')
    Gollum("I'm scared of lint errors.")
    Narrator('"Good!" thought a happy Python reviewer.')

No:
    Python("Why are you hiding your eyes?")
    Gollum('The lint. It burns. It burns us.')
    Gollum("Always the great lint. Watching. Watching.")
```

---

## 2.Naming 命名

(1) 不要以下面的关键字命名

```
False   class       finally     is          return
None    continue    for         lambda      try
True    def         from        nonlocal    while
and     del         global      not         with    
as      elif        if          or          yield
assert  else        import      pass
break   except      in          raise
```

(2) 记住

- 除了计数和迭代的变量, 其他不以单个字符(字母)命名
- 不用 `-` 来对 package or module 命名
- 不用 `__double_leading_and_trailing_underscore__` names (reserved by Python)

(3) 命名

```
module_name.py
package_name.py
ClassName
method_name
ExceptionName
function_name
GLOBAL_CONSTANT_NAME
global_var_name
instance_var_name
function_parameter_name
local_var_name
```

> Prepending a single underscore (_) has some support for protecting module variables and functions (not included with `import * from`). Prepending a double underscore (__) to an instance variable or method effectively serves to make the variable or method private to its class (using name mangling).

## 3.Importing Formatting

> (1) 每一行单独 import 库

```
Yes: import os
     import sys

No:  import os, sys
```

> (2) 在脚本顶端起始 import, 顺序

- 标准库 import
- 第三方库 import
- application-specific imports (特定应用程序的 import)

> (3) 每一组 import, 按字典顺序排列(字母顺序, 不计大小写, according to each module's full package path.), 比如

```
import foo
from foo import bar
from foo.bar import baz
from foo.bar import Quux
from Foob import ar
```

> (4) 莫要使用 ~~from foo import *~~

---

## 参考

- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html#Strings)
