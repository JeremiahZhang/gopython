# Tuples

- Like lists
- Immutable
- Things not to do with Tuples
- A tale of two sequences
- Assignment
- With dictionaries
- Comparable
- Sorting lists of tuples
- sorted()
- List comprehension

## Pythonic module

```
txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))

t.sort(reverse=True)

res = list()
for length, word in t:
    res.append(word)

print(res)

# Code: http://www.py4e.com/code3/soft.py
```

## Summary

- Tuple syntax
- Immutability
- Comparability
- Sorting
- Tuples in assignment statements
- Sorting dictionaries by either key or value
