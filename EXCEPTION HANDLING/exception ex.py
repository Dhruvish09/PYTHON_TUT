result=None
x=str(input('enter your 1st number:'))
y=str(input('enter your 2nd number:'))



try:
    result=int(x/y)
    
except Exception as e:
    print(e)
    
else:
    print("inside else block")
finally:
    print("inside finally block")
    
print("--new line--")
print("result:",result)