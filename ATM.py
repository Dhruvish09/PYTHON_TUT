print('WELCOME TO PATEL BANK OF ATM')
restart=('y')
chances = 3
balance = 999

while chances >=0:
    print("There are 3 try to available for enter your correct pin after that your card is gone for block for 24 hours!")
    pin=int(input('enter your 4 digit pin:'))
    if pin == (1234):
        print('you entered pin is correctly\n')
        while restart not in ('n','NO','no','N'):
            print('please press 1 for your Balance\n')
            print('please press 2 to make a withdrawl\n')
            print('please press 3 to pay in\n')
            print('please press 4 to return card\n')
            option =int(input('what would u like to choose?'))
            if option == 1:
                print('your Balance is rs',balance,'\n')
                restart =input('would you like to go back?')
                if restart in ('n','NO','no','N'):
                    print('Thank u')
                    break
            elif option==2:
                option=('y')
                withdrawl = float(input('how much would you like to withdraw?\nrs100/rs200,rs300'))
                if withdrawl in [100,200,300]:
                    balance = balance - withdrawl
                    print('your balance is now',balance)
                    restart=input('would u like to go back?')
                    if restart in ('n','NO','no','N'):
                        print('Thank u')
                        break
                elif withdrawl !=[100,200,300]:
                    print('Invalid Amount ,please Re-try\n')
                    restart=('y')
                elif withdrawl == 1:
                    withdrawl = float(input('please Enter Desired amount:'))

                elif option==3:
                     pay_in = float(input('How Much Would you like to Pay in?'))
                balance=balance+pay_in
                print('\nYour Balance is now',balance)
                restart=input('Would u like to go back?')
                if restart in ('n','NO','no','NO'):
                    print('Thank u')
                    break
                elif option==4:
                    print('please wait while your card is returned...\n')
                    print('Thank u for your service\n')
                break
            else:
                    print('please Enter a correct number. \n')
            restart=('y')
    if pin!=('1234'):
        print('Incorret Password')
        chances=chances-1
        if chances == 0:
            print('\nNo more tries')
            break




