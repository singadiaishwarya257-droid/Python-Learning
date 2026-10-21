# Python OOP Concepts — W3Schools Learning Notes

**Learning source:** [W3Schools Python OOP](https://www.w3schools.com/python/python_classes.asp)  
**Topic sequence:** Python OOP → Classes and Objects → `__init__()` → `self` → Class Properties → Class Methods → Magic Methods → Inheritance → Polymorphism → Encapsulation → Inner Classes

These are concise study notes with practical examples, following the W3Schools Python OOP topic sequence.

## Contents

1. [Python OOP](#1-python-oop)
2. [Classes and Objects](#2-python-classes-and-objects)
3. [`__init__()` Method](#3-python-__init__-method)
4. [`self` Parameter](#4-python-self-parameter)
5. [Class Properties](#5-python-class-properties)
6. [Class Methods](#6-python-class-methods)
7. [Magic Methods](#7-python-magic-methods)
8. [Inheritance](#8-python-inheritance)
9. [Polymorphism](#9-python-polymorphism)
10. [Encapsulation](#10-python-encapsulation)
11. [Inner Classes](#11-python-inner-classes)
12. [Manual Data Flow](#manual-data-flow)
13. [Quick Revision](#quick-revision)
14. [Learning Progress](#learning-progress)

## 1. Python OOP

OOP stands for **Object-Oriented Programming**. It organizes code around classes and objects.

### Why use OOP?

- Organizes code into clear structures.
- Helps reuse code.
- Makes programs easier to maintain and extend.
- Keeps related data and behavior together.

### Main OOP pillars

- **Encapsulation:** Keep data and related methods together, and control access to data.
- **Inheritance:** Create a class based on another class to reuse and extend functionality.
- **Polymorphism:** Use a common interface with different behaviors.
- **Abstraction:** Show essential features while hiding implementation details.

## 2. Python Classes and Objects

A **class** is a blueprint for creating objects. An **object** is an instance of a class.

```python
class Student:
    school = "KLE"


student1 = Student()
print(student1.school)
```

**Output**

```text
KLE
```

### Important points

- Use the `class` keyword to define a class.
- Create an object by calling the class, such as `Student()`.
- An object can have attributes (data) and methods (functions defined in a class).
- You can create multiple objects from one class.
- `pass` can be used when a class body is temporarily empty.
- `del object_name` deletes a reference to an object.

### Multiple objects

```python
class Student:
    school = "KLE"


student1 = Student()
student2 = Student()

print(student1.school)
print(student2.school)
```

**Output**

```text
KLE
KLE
```

## 3. Python `__init__()` Method

`__init__()` is a special method that Python calls automatically when a new object is created. It is commonly used to initialize an object's attributes.

```python
class Student:
    def __init__(self, name, semester):
        self.name = name
        self.semester = semester


student1 = Student("Asha", 5)
print(student1.name)
print(student1.semester)
```

**Output**

```text
Asha
5
```

### Key points

- `__init__` begins and ends with double underscores.
- It runs automatically during object creation.
- Parameters can be passed when creating an object.
- `self.name` and `self.semester` store data on that particular object.
- Technically, `__init__()` initializes an already-created object; it is not the method that creates the object itself.

## 4. Python `self` Parameter

`self` refers to the current object instance. It lets an instance method access that object's attributes and other methods.

```python
class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)


student1 = Student("Asha")
student1.introduce()
```

**Output**

```text
My name is Asha
```

### Key points

- `self` is the conventional parameter name; it is not a Python keyword.
- It is the first parameter in a normal instance method.
- When calling `student1.introduce()`, Python supplies `student1` as the instance argument automatically.
- `self.name` means the `name` attribute belonging to the current object.

## 5. Python Class Properties

Properties are values associated with a class or its objects. In Python, “property” can refer broadly to attributes, and `@property` can also create managed attributes.

### Instance attributes

Each object can store its own values.

```python
class Student:
    def __init__(self, name):
        self.name = name


student1 = Student("Asha")
student2 = Student("Ravi")

print(student1.name)
print(student2.name)
```

**Output**

```text
Asha
Ravi
```

### Class attributes

A class attribute is defined directly inside the class and is commonly shared by its instances.

```python
class Student:
    school = "KLE"


student1 = Student()
student2 = Student()

print(student1.school)
print(student2.school)
```

**Output**

```text
KLE
KLE
```

### Using `@property`

```python
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price


item = Product(250)
print(item.price)
```

**Output**

```text
250
```

`@property` lets a method be accessed like an attribute. A setter can be added when controlled updates are needed.

## 6. Python Class Methods

Methods are functions defined inside a class.

- **Instance method:** Uses `self` to work with an individual object.
- **Class method:** Uses `cls` to work with class-level data. It is marked with `@classmethod`.
- **Static method:** Does not automatically receive `self` or `cls`. It is marked with `@staticmethod` and is useful for related utility behavior.

```python
class Student:
    school = "KLE"

    def __init__(self, name):
        self.name = name

    def show_name(self):
        return self.name

    @classmethod
    def show_school(cls):
        return cls.school

    @staticmethod
    def is_adult(age):
        return age >= 18


student1 = Student("Asha")
print(student1.show_name())
print(Student.show_school())
print(Student.is_adult(20))
```

**Output**

```text
Asha
KLE
True
```

## 7. Python Magic Methods

Magic methods, also called **dunder methods**, have names that begin and end with double underscores. They let objects work with built-in operations and functions.

| Method | Purpose |
| --- | --- |
| `__str__()` | Provides a user-friendly string representation. |
| `__repr__()` | Provides a developer-oriented representation. |
| `__eq__()` | Defines behavior for `==`. |
| `__add__()` | Defines behavior for `+`. |
| `__len__()` | Defines behavior for `len()`. |
| `__lt__()` | Defines behavior for `<`. |
| `__contains__()` | Defines membership behavior such as `in`. |
| `__call__()` | Lets an object be called like a function. |

### Example: `__str__()` and `__add__()`

```python
class Number:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __add__(self, other):
        return Number(self.value + other.value)


first = Number(10)
second = Number(5)

print(first)
print(first + second)
```

**Output**

```text
10
15
```

In this example, `__add__()` returns another `Number` object, and `__str__()` controls how that object is printed.

## 8. Python Inheritance

Inheritance lets a child class reuse and extend attributes and methods from a parent class.

```python
class Animal:
    def speak(self):
        print("Animal sound")


class Dog(Animal):
    def bark(self):
        print("Woof!")


dog = Dog()
dog.speak()
dog.bark()
```

**Output**

```text
Animal sound
Woof!
```

### Important terms

- **Parent/base class:** The class being inherited from.
- **Child/derived class:** The class that inherits.
- `super()` can call parent-class behavior, often to initialize parent attributes.
- A child class can add methods or override inherited methods.

### Common inheritance forms

- Single inheritance
- Multiple inheritance
- Multilevel inheritance
- Hierarchical inheritance

## 9. Python Polymorphism

Polymorphism means “many forms.” A common method name or interface can produce different behavior for different objects.

### Example: method overriding

```python
class Dog:
    def speak(self):
        print("Woof!")


class Cat:
    def speak(self):
        print("Meow!")


for animal in (Dog(), Cat()):
    animal.speak()
```

**Output**

```text
Woof!
Meow!
```

Both objects provide `speak()`, but each implementation behaves differently.

## 10. Python Encapsulation

Encapsulation groups data and methods in a class and helps control how internal data is accessed or changed.

### Naming conventions

- `name` — public attribute.
- `_name` — conventionally intended for internal or protected use.
- `__name` — triggers name mangling; it is not absolute security.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount


account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())
```

**Output**

```text
1500
```

### Key points

- Keep data and related operations together.
- Use methods to validate updates.
- A double underscore causes name mangling, rather than making data completely inaccessible.
- Avoid directly changing internal data when a method can enforce rules.

## 11. Python Inner Classes

An inner class is a class defined inside another class. It can be useful when a helper class is closely related to the outer class.

```python
class Computer:
    def __init__(self, brand):
        self.brand = brand
        self.processor = self.Processor("i5")

    class Processor:
        def __init__(self, model):
            self.model = model


computer = Computer("Dell")
print(computer.brand)
print(computer.processor.model)
```

**Output**

```text
Dell
i5
```

### Key points

- `Processor` is defined inside `Computer`.
- The inner class can be referred to as `Computer.Processor`.
- Defining a class inside another class does not automatically give it access to an outer object's instance attributes; pass any required data explicitly.

## Manual Data Flow

```text
Class (blueprint)
      ↓
Object creation
      ↓
__init__() initializes attributes
      ↓
self accesses the current object
      ↓
Methods use or update data
      ↓
Output / result
```

## Quick Revision

| Topic | Remember |
| --- | --- |
| OOP | Organizes code around objects. |
| Class | Blueprint for objects. |
| Object | Instance of a class. |
| `__init__()` | Initializes object attributes. |
| `self` | Refers to the current instance. |
| Class attribute | Shared class-level value, unless shadowed. |
| Class method | Receives `cls`. |
| Magic method | Customizes built-in operations. |
| Inheritance | Reuses and extends a class. |
| Polymorphism | Same interface, different behavior. |
| Encapsulation | Controls access to internal data. |
| Inner class | Class defined inside another class. |

## Learning Progress

- [ ] Python OOP
- [ ] Classes and Objects
- [ ] `__init__()` Method
- [ ] `self` Parameter
- [ ] Class Properties
- [ ] Class Methods
- [ ] Magic Methods
- [ ] Inheritance
- [ ] Polymorphism
- [ ] Encapsulation
- [ ] Inner Classes

**Suggested Git commit message:** `docs: add Python OOP notes from W3Schools`
