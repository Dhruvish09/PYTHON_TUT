
# Python allows you to assign values to multiple variables in one line:

# Many Values to Multiple Variables
print("Program 1 Output:")
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z,end='\n\n')

# One value to multiple variables:
print("Program 2 Output:")
x = y = z = "Orange"
print(x)
print(y)
print(z,end='\n\n')

# Unpack a Collection
print("Program 3 Output:")
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)