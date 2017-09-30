# 代码风格

积累, 规范代码风格

# string

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


# 参考

- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html#Strings)
