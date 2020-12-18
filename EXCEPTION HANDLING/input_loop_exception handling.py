try:
    Name=str(input("Enter your Name:"))
except Exception as e:
    print(e)
else:
    print("Hello Sir your Name is",Name)
finally:
    pass
    
try:
    Age=int(input("Enter your Age:"))
except Exception as e:
    print(e)
else:
    print("Sir your Age is",Age)
    if Age>18:
        print("Sir you are adult")
    elif Age<18:
        print("Sir you are teenager")
finally:
    pass
     
try:
    Weight=float(input("Enter your Weight:"))
except Exception as e:
    print(e)
else:
    print("Sir your  Weight is",Weight)
    if Weight>100:
        print("Sir you want to do excercise and follow diet...")
    elif Weight<80:
        print("Sir you are fit")
finally:
    pass