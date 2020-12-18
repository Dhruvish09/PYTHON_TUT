
# try:
#     Age=int(input("Enter Your Age:"))
# except Exception as e:
#     print(e)
# else:
#     if Age>0:
#         print("Your Age is",Age,"Congratulation u r human")
#     elif Age<0:
#         print("Your Age is",Age,"your are Alien!")
#     else:
#         pass
# finally:
#     print("Done your fillup!")


Age=int(input("Enter Your Age:"))
try:
    if Age>0:
        print("Age is Positive")
    elif Age<0:
        print("Your Age is Negative")
    else:
        pass
except Exception as e:
    print(e)
else:
    pass
finally:
    print("Done your data!")
    