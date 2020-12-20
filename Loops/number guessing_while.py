import random
n=20
to_be_guessed=int(n*random.random())+1
guess=0
while guess!=to_be_guessed:
    guess=int(input("new number:"))
    if guess>0:
        if guess>to_be_guessed:
            print("number is too large ")
        elif guess<to_be_guessed:
            print("number is too small")
        else:
            print("sorry that u'r giving  up!")
            break
    else:
        print("congreee!. you made it!!!")
