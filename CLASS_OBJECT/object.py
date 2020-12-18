#Now we can use the class named MyClass to create objects:

class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

#You can modify properties on objects like this:
class Person:
      def __init__(self, name, age):
          self.name = name
          self.age = age

def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.age = 40

print(p1.age)

#You can delete properties on objects by using the del keyword:
class Person:
      def __init__(self, name, age):
          self.name = name
          self.age = age

def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

# del p1.age

print(p1.age)

#

