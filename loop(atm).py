print('Welcome to SBI')
balance=1000
trys=0
restart='y'
while trys<=3:
    username = input("enter username:")
    if username=="manu":
        pin = int(input('enter pin :'))
        if pin==2462:
            while restart not in ('n','N'):
                print("welcome",username)
                print("press 1 for balance check")
                print("press 2 for withdraw")


                option=int(input("enter chooice"))
                print(" ")

                if option == 1:
                    print("your balance is:",balance)
                    restart=input("do you want to continue(y/n)")
                if restart in('n','N'):
                    print("thank you for your visit")
                    exit()

                elif option == 2:
                    restart = ('y')
                    amount=int(input("enter the amount"))
                    if amount in [100,200,500,2000]:
                        if balance<amount:
                            print("insufficient amount" )
                            restart=("y")

                            balance=balance-amount
                            print("Current balance is",balance )
                            restart = input("do you want to continue(y/n)")
                    if restart in ('n', 'N'):
                        print("thank you for your visit")

                    elif amount!=[100,200,500,2000]:
                        print(" please try again and enter 100,200,500,,1000,2000\n")
                        restart=('y')
                        option ==2

        else:
            trys += 1
            print("pin in incorrect",3-trys,"left")
            if trys ==0:
                print("contact to bank")



    else:
        print("username is incorrect")


