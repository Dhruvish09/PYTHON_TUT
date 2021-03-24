# def age_counter():
#     seconds_or_years = input("Enter your seconds (s) or years (y)?")
#     if seconds_or_years == "s":
#         user_value = input("Enter the number of seconds you've lived for")
#         print("You've lived for {} years".format(int(user_value)/60/60/24/365))
    
#     elif seconds_or_years == "y":
#         user_value = input("Enter the number of years you've lived for:")
#         print("you've lived for {} seconds".format(int(user_value)*365*24*60*60))
        
# age_counter()
try:
    age=int(input("Enter your age:"))
except Exception as e:
    print(e)
else:
    if age<18:
        print("You are teenage")
    elif age>18:
        print("You are adult")
    else:
        print("under process")
finally:
    print("have greate day")

