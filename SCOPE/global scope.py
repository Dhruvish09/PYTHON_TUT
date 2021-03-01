#A variable created in the main body of the Python code is a global variable and belongs to the global scope.

x = 300

def myfunc():
  print(x)

myfunc()

print(x)