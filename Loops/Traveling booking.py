travelling=input("yes or no!")

while travelling=='yes':
    num= int(input("number of people travelling:"))
    
    for num in range(1,num+1):
        name=input("name:")
        age=input("age:")
        sex=input("male or femal:")
        print(name)
        print(age)
        print(sex) 
        
    travelling=input("oops! forgot someone:")
   
  