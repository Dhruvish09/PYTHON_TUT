#If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

def myfunc():
      global x
      x=300

myfunc()

print(x)
