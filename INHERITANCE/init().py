#So far we have created a child class that inherits the properties and methods from its parent.

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname):
#     Person.__init__(self, fname, lname)

x = Person("Mike", "Olsen")
print(x.firstname)
print(x.lastname)

