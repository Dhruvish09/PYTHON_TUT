#To create a class, use the keyword class:

# class MyClass:
#   x = 5

# print(MyClass)

#
class Person:
      def __init__(self, name, age):
            self.name = name
            self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)



class Collage:
    def __init__(self,data):
        self.name = data["name"]
        self.age = data["age"]

data_list = [{"name":"Dhruvidh","age":24},{"name":"Tirth","age":25}]

data = [Collage(data) for data in data_list]

for value in data:
    print(f"Name: {value.name} and Age:{value.age}")