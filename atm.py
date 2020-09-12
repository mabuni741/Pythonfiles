
a = 0
while a<3:
    pin=input("Enter pin value:-")
    if pin=="1234":
        account=input("Enter Account type:-")
        if account=="savings":
            amount=input("Enter the Amount:-")
            if amount <="5000":
                print("Transaction is Successfull")
                break    
            else:
                print("Insuffcient Funds")
                a=a+1
        elif account=="current":
            print("current account is activated")
            break
        elif account=="personal":
            print("check balance")   
            break
        else:
            print("Account type invalid")
            a=a+1
    else:
        a=a+1   
        #if a != 3:
        print("ur pin is invalid, please try again") 
else:
    print("Your account is blocked for 24 hours")
       
















