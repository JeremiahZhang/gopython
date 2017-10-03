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
