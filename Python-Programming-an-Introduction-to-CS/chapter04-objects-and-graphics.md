# 第四章: 对象与图形界面

- 目标:
    - 理解 objects 概念, 以及它们如何简化编程.
    - To be familiar with the various objects available in the graphics library.
    - To be able to create objects in programs and call appropriate methods to perform graphical computations.
    - To understand the fundamental concepts of computer graphics, especially the role of coordinate systems and coordinate transformations.
    - To understand how to work with both mouse and text-based input in a graphical programming context.
    - To be able to write simple interactive graphics programs using the graphics library.
- summary:
    - An object is a computational entity that combines data and operations. An object's data is stored in instance variables, and its operations are called methods.
    - Every object is an instance of some class. It is the class that determines what methods an object will have. An instance is created by calling a constructor method.
    - An object's attributes are accessed via dot notation. Generally computations with objects are performed by calling on an object's methods. Accessor methods return information about the instance variables. Mutator methods change the value(s) of instance variables.
    - The graphics module supplied with this book provides a number of classes that are useful for graphics programming.
    - An important consideration in graphical programming is the choice of an appropriate coordinate system. The graphics library provides a way of automating certain coordinate transformations.
    - The situation where 2 variables refer to the same object is called aliasing. It can sometimes cause unexpected results. Use the `clone` method in the graphics library can help prevent these situations.

---

## 1.The object of objects.

> objects know stuff(they contain data), and they can do stuff(they have operations).

> objects may refer to other objects.

---

## 2.Simple graphics programming

```
>>> from graphics import *
>>> win = GraphWin()
>>> p = Point(50, 60)
>>> p.getX()
50.0
>>> p.getY()
60.0
>>> p.draw(win)
Point(50.0, 60.0)
>>> p2 = Point(140, 100)
>>> p2.draw(win)
Point(140.0, 100.0)
>>> win.close()
>>> win = GraphWin("Shapes")
>>> win
GraphWin('Shapes', 200, 200)
>>> center = Point(100, 100)
>>> circ = Circle(center, 30)
>>> circ.setFill("red")
>>> circ.draw(win)
Circle(Point(100.0, 100.0), 30)
>>> label = Text(center, "Red Circle")
>>> lable.draw(win)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'lable' is not defined
>>> label.draw(win)
Text(Point(100.0, 100.0), 'Red Circle')
>>> rect = Rectangle(Point(30, 30), Point(70, 70))
>>> rect.draw(win)
Rectangle(Point(30.0, 30.0), Point(70.0, 70.0))
>>> line = Line(Point(20, 30), Point(180, 199))
>>> line.draw(win)
Line(Point(20.0, 30.0), Point(180.0, 199.0))
>>> oval = Oval(Point(20, 150), Point(180, 199))
>>> oval.draw(win)
Oval(Point(20.0, 150.0), Point(180.0, 199.0))
```

## 3.Using graphical objects

> Objects combine data with operations.

> Every object is an instance of some class, and the class describes the properties the instance will have.

- 类比:
    - 狗
        - Fido(狗的名字)
            - 属性:
                - four legs
                - a tail
                - a cold, wet nose
                - barks.
                - ...
        - Rex(狗的名字)
            - 属性(同上)
    - Class
        - instance
            - attribute(-- function)

> 建立: To create a new instance of a class, we use a special operation called a **constructor**.

```
<ClassName>(<param1>, <param2>, ...)
```

- **instance variables**

![1](https://dn-learnml.qbox.me/image/programming/ppai2cs_ch04_04_class_instance.png)

- **methods**

```
<object>.<method_name>(<param1>, <param2>, ...)
```

> Methods that change the state of an object are sometimes called **mutators**(变异).

```
from graphics import *

circ = Circle(Point(100, 100), 30)
win = GraphWin()
cric.draw(win)
```

流程:

![2](https://dn-learnml.qbox.me/image/programming/ppai2cs_ch04_05_object_interaction_example.png)

> 小心同名. It is possible for two different variables to refer to exactly the same object; changes made to the objext throught on variable will also visible to the other.

案例:

```
## Incorrect way to create two circles.
leftEye = Circle(Point(80, 50), 5)
leftEye.setFill('yellow')
leftEye.setOutline('red')

rightEye = leftEye
rightEye.move(20, 0)
```

**最后一行代码, 将两个 instance 都移动, 因为两个 instances refer to exactly the same object 'Circle'**. 看下图说明

![3](https://dn-learnml.qbox.me/image/programming/ppai2cs_ch04_06_aliases.png)

`leftEye, rightEye` 同名(object).

> The situation where two variables refer to the same object is called **aliasing**, and it can sometimes produce rather unexpected results.

`rightEye` 不要直接用 赋值 `=` 去 copy `leftEye`. 而是要按如下的方法:

```
## A correct way to create two circle.
leftEye = Circle(Point(80, 50), 5)
leftEye.setFill('yellow')
leftEye.setOutline('red')

rightEye = Circle(Point(80, 50), 5)
rightEye.setFill('yellow')
rightEye.setOutline('red')
```

上面的方法是不是有点冗余, 还有一种优雅的方法:(all graphical objects support a `clone` method that makes a copy of the object.)

```
## Correct way to create two circles, using clone
leftEye = Circle(Point(80, 50), 5)
leftEye.setFill('yellow')
leftEye.setOutline('red')

# rightEye is an exact copy of the left
rightEye = leftEye.clone()
rightEye.move(20, 0)
```

---

## 4.Graphing future value

投资的复利 图形化.

**Specification**:

```
Print an introduction
Get value of principal and apr from usr
Create a GraphWin
Draw scale labels on left side of window  
Draw bar at position 0 with height corresponding to principal  
for successive years 1 throught 10
    Calculate principal = principal * (1 + apr)
    Draw a bar for this year having a height corresponding to principal
Wait for usr to press Enter.
```

推进  

```
Print an introduction
Get value of principal and apr from user
Create a 320x240 GraphWin titled ‘‘Investment Growth Chart’’
Draw label " 0.0K" at (20, 230)
Draw label " 2.5K" at (20, 180)
Draw label " 5.0K" at (20, 130)
Draw label " 7.5K" at (20, 80)
Draw label "10.0K" at (20, 30)
Draw a rectangle from (40, 230) to (65, 230 - principal * 0.02)
for year running from a value of 1 up through 10:
    Calculate principal = principal * (1 + apr)
    Calculate xll = 25 * year + 40
    Draw a rectangle from (xll, 230) to (xll+25, 230 - principal * 0.02)

Wait for user to press Enter
```

![4](https://dn-learnml.qbox.me/image/programming/ppai2cs_ch04_coding_results.png)
