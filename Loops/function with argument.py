#Information can be passed into functions as arguments.

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus") 

#You can also send arguments with the key = value syntax.
def my_function(child3, child2, child1):
      print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#If we call the function without argument, it uses the default value:
def my_function(country = "Norway"):
      print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil") 

#You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
def my_function(food):
      for x in food:
          print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#To let a function return a value, use the return statement:
def my_function(x):
      return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9)) 

