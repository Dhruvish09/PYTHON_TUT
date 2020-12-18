#When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
#These exceptions can be handled using the try statement:
#The try block will generate an error, because x is not defined:
x=21
y=1
try:
  print(x/y)
except:
  print("An exception occurred")
