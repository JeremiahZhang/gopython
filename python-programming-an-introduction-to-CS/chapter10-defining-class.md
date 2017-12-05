# 第10章 Class

- 目标:
    - Defining new classes
    - Read and write Python class definitions
        - `__doc__`
        - `help()`
        - `print(<module_name>.__doc__)`
            - `import pydoc`
            - `print(pydoc.__doc__)`
            - `help(pydoc)`  
    - The concept of encapsulation
    - Write programs involving simple class definitions
    - Write interactive graphics programs involving novel widgets.

---

# coding

```
>>> import cball2.py
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'cball2.py'; 'cball2' is not a package
>>> import cball2
>>> print(cabll2.Projectle.__doc__)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'cabll2' is not defined
>>> print(cball2.Projectle.__doc__)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'cball2' has no attribute 'Projectle'
>>> print(cball2.Projectile.__doc__)
Simulates the flight of simple projectiles near the earth's
    surface, ignoring wind resistance. Tracking is done in two
    dimensions, height (y) and distance (x).

    Attributes:
        angle: A number representing lanuch angle.
        velocity: A number representing initial velocity.
        height: A number representing initial height.

>>> help(projectile)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'projectile' is not defined
>>> help(cball2)
Help on module cball2:

NAME
    cball2

DESCRIPTION
    cball2.py
    Provides a simple class for modeling the
    flight of projectiles.

CLASSES
    builtins.object
        Projectile

    class Projectile(builtins.object)
     |  Simulates the flight of simple projectiles near the earth's
     |  surface, ignoring wind resistance. Tracking is done in two
     |  dimensions, height (y) and distance (x).
     |
     |  Attributes:
     |      angle: A number representing lanuch angle.
     |      velocity: A number representing initial velocity.
     |      height: A number representing initial height.
     |
     |  Methods defined here:
     |
     |  __init__(self, angle, velocity, height)
     |      Create a projectile with given lanuch angle, initial
     |      velocity and height.
     |
     |  get_x(self)
     |      Returns the x position (distance) of this projectile.
     |
     |  get_y(self)
     |      Returns the y position (height) of this projectile.
     |
     |  update(self, time)
     |      Update the state of this projectile to move it time seconds
     |      farther into its flight.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)

FUNCTIONS
    cos(...)
        cos(x)

        Return the cosine of x (measured in radians).

    get_input()

    main()

    radians(...)
        radians(x)

        Convert angle x from degrees to radians.

    sin(...)
        sin(x)

        Return the sine of x (measured in radians).

FILE
    e:\2016-for_vocation\gopython\python-programming-an-introduction-to-cs\src\ch10\cball2.py
```

bug:

```
[ten_years] PS E:\2016-for_Vocation\gopython\Python-Programming-an-Introduction-to-CS\src\ch10> python .\roller.py
<class 'ch04.graphics.Point'>
1
<class 'ch04.graphics.Point'>
1
<class 'method'>
1
Traceback (most recent call last):
  File ".\roller.py", line 49, in <module>
    main()
  File ".\roller.py", line 35, in main
    while not quit_button.clicked(pt):
  File "E:\2016-for_Vocation\gopython\Python-Programming-an-Introduction-to-CS\src\ch10\button.py", line 51, in clicked
    p_x = p.getX()
AttributeError: 'function' object has no attribute 'getX'
```

原来是:

```
while not quit_button.clicked(pt):
    if roll_button.clicked(pt):
        value1 = randrange(1, 7)
        die1.set_value(value1)
        value2 = randrange(1, 7)
        die2.set_value(value2)
        quit_button.activate()

    pt = win.getMouse()
    # 之前 写成了 pt = win.getMouse
    # 所以才会有 <class 'method'> 出现
```

看报错信息, 阅读代码上下文, 检查错误, 是用`print`来看看.

# summary

- Object
    - data
    - manipulate that data
    - methods
- Object = Instance of class
- Class
    - a collection of function definitions
    - `__init__(self, arg)`
    - `def <methods_name>(self, arg)`
- `__init__` special method is the constructor for a class
    - To initialize the instance variables of an object.
- Instance variables of an object should only be accessed or modified throught the interface methods of the class.
