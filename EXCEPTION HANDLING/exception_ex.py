def enter_num():
    while True:
        try:
            result=int(input("enter a number"))
        except:
            print("you are not entered number")
            continue
        else:
            print("thank u so much")
            break
        finally:
            print("i am alwase with you!")
    
my_function=enter_num         #Decorator
my_function()
