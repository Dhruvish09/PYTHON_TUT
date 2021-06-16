# Create a variable outside of a function, and use it inside the function
print("(1) Program:")
a= 12
b=2
                                                    
def sum():
    print(a/b,end='\n\n')
sum()


print("(2) Program:")
x = "awesome"

def myfunc():
  print("Python is " + x,end='\n\n')

myfunc()

# Create a variable inside a function, with the same name as the global variable
print("(3) Program:")
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x,end='\n\n') 

# If you use the global keyword, the variable belongs to the global scope:
print("(4) Program:")
def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x,end='\n\n')
