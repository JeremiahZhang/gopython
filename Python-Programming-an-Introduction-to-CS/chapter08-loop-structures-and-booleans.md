# 第8章 loop 结构和布尔 booleans

- 目标:
    - Definite and indefinite loops
        - `for` - definite
        - `while` - indefinite
    - 5+ Programming patterns interactive loop and sentinel loop        
        - their implementation using a Python `while` statement
    - 5+ Programming patterns end-of-file loop and ways of implementation such loops in Python
    - Design and implement solutions involving loop patterns including nested loop structures.
    - Basic ideas of Boolean algebra and be able to analyze and write Boolean expressions involving Boolean operators.

---

## 1.For loops

```
for <var> in <sequence>:
    <body>
```

`average1.py` simple for loop. 容易理解.

---

## 2.Indefinite Loops

`conditional loop`

```
while <condition>:
    <body>
```

Avoid writing indefinite loops in the first place.

---

## 3.Common Loop Patterns

- Interactive loops

```
set moredata to "yes"
while moredata is "yes":
    get the next data item
    process the item
    ask user if there is moredata
```

- Sentinel loops

```
get the first data item
while item is not the sentinel
    process the item
    get the next data item
```

- File loops  
    - `for line in infile`
    - `readline()` end-of-file loop
- Nested loops

---

## 4.Computing with Booleans

- Boolean operators

```
<expr> and <expr>

<expr> or <expr>
```

顺序: 高-->低 `not, and, or`

`a or not b and c` == `(a or ((not b) and c))`

- Boolean algebra

| Algebra | Boolean Algebra     |
| :------------- | :------------- |
| a * 0 = 0      | a and false == false |
| a * 1 = a      | a and true == a      |
| a + 0 = a      | a or false == a      |

`a or true == true`  
`a or (b and c) == (a or b) and (a or c)`  
`a and (b or c) == (a and b) or (a and c)`

`not (not a) == a`

**DeMorgan's Law**  

`not (a or b) == (not a) and (not b)`
`not (a and b) == (not a) or (not b)`

```
while (not scoreA = 15) and (not scoreB = 15):
    # continue playing

while scoreA != 15 and scoreB != 15:
    # continue playing
```

---

## 5.Other Common Structures

- Post-Test Loop  

`input validation`

```
repeat
    get a number from the user

until number is >= 0
```

in Python

```
number = -1 # Start with an illegal value to get into the loop
while number < 0:
    number = eval(input("Enter a positive number: "))
```

or + `whlie ture + break`

```
while True:
    x = eval(input("Enter a positive number: "))
    if x >= 0:
        break
    else:
        print("The number you enter was note positive.")
```

- Loop and a Half.

```
while True:
    x = eval(input("Please enter a positive number: "))
    if x >= 0: break # Loop exit in the middle of the loop body: a loop and a half
    print("The number you entered was not positive.")
```

> Should be avoided is peppering the body of a loop with multiple **break** statements. The logic of a loop is easily lost when there are multiple exits. However, there are times when even this rule should be broken to provide the most elegant solutuion to a problem.

---
