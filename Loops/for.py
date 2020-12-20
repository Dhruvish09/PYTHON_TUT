#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
#With the break statement we can stop the loop before it has looped through all the items:
  print('{BREAK STATEMENT:}')
  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#With the continue statement we can stop the current iteration of the loop, and continue with the next:fruits = ["apple", "banana", "cherry"]
print('{COUNTINUE STATEMENT:}')
for x in fruits:
  if x == "banana":
    continue
  print(x)
  
#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
print('{RANGE() FUNCTION:}')
for x in range(2,6):
      print(x) 
      
else:
      print("Finally finished!")
      
 #A nested loop is a loop inside a loop.
print('{NESTED LOOP:}')
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) 
    
#for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
print('{PASS:}')
for x in [0, 1, 2]:
      pass
  
