# 🐍 Python OOP Concepts & Core Constructs

---

## 1. What is Object-Oriented Programming (OOP)?

**Answer:**

Object-Oriented Programming is a programming paradigm that organizes code into **objects**, which are instances of **classes**.
It revolves around the principles of:

* **Encapsulation**: Bundling data and methods.
* **Inheritance**: Reusing code via parent-child class relationships.
* **Polymorphism**: Methods behaving differently based on the object.

> 💡 OOP allows developers to model real-world entities and their interactions effectively.

---

## 2. What is a Module in Python?

**Answer:**

A **module** in Python is a `.py` file containing variables, functions, or classes.
Modules enable **code organization** and **reuse** by grouping related functionalities.

### 📦 Types of Modules:

* **Built-in Modules**: Part of Python standard library.

  ```python
  import math
  import os
  ```

* **Third-Party Modules**: Installed via `pip`.

  ```bash
  pip install requests
  ```

  ```python
  import requests
  ```

* **Custom/User-Defined Modules**: Created by the user to reuse custom logic.

---

## 3. What is `__init__`?

**Answer:**

`__init__` is a **constructor method** in Python that runs **automatically** when a class object is instantiated.

### 🔧 Example:

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

my_car = Car("Toyota", "Camry", 2022)
```

---

## 4. Python Class and Functions

**Answer:**

### 📘 Class:

A class is a blueprint to create objects (instances).

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")
```

```python
my_dog = Dog("Buddy")
my_dog.bark()
```

### 🧩 Function:

A function is a reusable block of code.

```python
def add(x, y):
    return x + y
```

---

## 5. What are Instance and Class Variables?

**Answer:**

### 🧍‍♂️ Instance Variables:

Belong to the **object** and are defined using `self`.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand      # Instance variable
        self.model = model
```

### 🧪 Class Variables:

Shared across **all instances** and defined at the **class level**.

```python
class Circle:
    pi = 3.14  # Class variable

    def __init__(self, radius):
        self.radius = radius  # Instance variable
```

---

## 6. What are Static and Class Methods?

**Answer:**

### ⚙️ Static Methods:

* Do **not** depend on instance or class.
* Use `@staticmethod`.

```python
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

result = MathOperations.add(3, 4)
```

### 🏫 Class Methods:

* Operate on the class itself.
* Use `@classmethod`.

```python
class Employee:
    total_employees = 0

    def __init__(self, name):
        self.name = name
        Employee.total_employees += 1

    @classmethod
    def get_total_employees(cls):
        return cls.total_employees

emp1 = Employee("Alice")
emp2 = Employee("Bob")
total = Employee.get_total_employees()
```

---

## 7. Can We Assign Multiple Constructors in Python?

**Answer:**

Python does **not support method overloading** by default, but you can simulate multiple constructors using `*args`.

### 🧠 Example:

```python
class Animal:
    def __init__(self, *args):
        if len(args) == 1:
            self.name = args[0]
        elif len(args) == 2:
            self.name, self.species = args
        elif len(args) == 3:
            self.name, self.species, self.age = args

    def make_sound(self, sound):
        return f"The animal is {self.name} and says {sound}"
```

```python
dog = Animal("dog", "mammals", 17)

print(dog.name)           # dog
print(dog.species)        # mammals
print(dog.age)            # 17
print(dog.make_sound("woof woof"))  # The animal is dog and says woof woof
```

---