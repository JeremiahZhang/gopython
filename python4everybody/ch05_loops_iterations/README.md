# Iteration

## Updating variables

```
x = x + 1
```

## The while statement

```
n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')
```

## Infinite loops

```
n = 10
while True:
    print(n, end=' ')
    n = n - 1
print('Done!')
```

break

```
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')
```

## Finishing iterations with continue

```
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)

print('Done')
```

输出:

```
> hello
hello
> # wolr
> hello
hello
> done
Done
```

## Definite loops using for

```
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')
```

## Loop patterns 

```
- Initializing one or more variables before the loop starts
- Performing some computation on each item in the loop body,   
possibly changing the variables in the body of the loop
- Looking at the resulting variables when the loop completes
```

## counting and summing loops

counting

```
count = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    count = count + 1
print('Count: ', count)
```

summing

```
total = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    total = total + itervar
print('Total: ', total)
```

## Maximum and minimum loops

```
largest = None
print('Before: ', largest)
for i in [3, 4, 12, 9, 74, 15]:
    if largest is None or i > largest:
        largest = i
    print('Loop: ', i, largest)
print('Largest:', largest)
```

```
smallest = None
print('Before:', smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print('Loop:', itervar, smallest)
print('Smallest:', smallest)

```

```
def min(values):
    smallest = None
    for value in values:
        if smallest is None or value < smallest:
            smallest = value
    return smallest
```

## debugging

二分法检查代码bug.

---
