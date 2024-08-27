# Encapsulation is the concept in object-oriented programming where the internal state of an object is hidden from the outside world, and access to it is restricted to well-defined methods. 
# It helps ensure data integrity, enhances security, and promotes code flexibility by providing a clear and controlled interface for interacting with objects.

# Public Encapsulation

class Person:
    def __init__(self, name, age):
        self.name = name  # Public attribute
        self.age = age    # Public attribute

    def display_info(self):
        print(f"The Encapsulation name is {self.name} and the age is {self.age}. (Public)")

person = Person("Public", 22)
person.display_info()


# Private Encapsulation

class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    def display_info(self):
        print(f"The Encapsulation name is {self.__name} and the age is {self.__age}. (Private)")

person = Person("Private", 23)
person.display_info()


# Protected Encapsulation

class Person:
    def __init__(self, name, age):
        self._name = name  # Protected attribute
        self._age = age    # Protected attribute

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def display_info(self):
        print(f"The Encapsulation name is {self._name} and the age is {self._age}. (Protected)")

student1 = Student("Protected", 24)
student1.display_info()