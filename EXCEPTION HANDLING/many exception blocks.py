#You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:

#The try block will generate a NameError, because x is not defined:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")