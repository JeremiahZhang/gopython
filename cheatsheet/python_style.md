# 代码风格

积累, 规范代码风格

---

## String 字符串

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

## Name 命名

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


## 参考

- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html#Strings)
