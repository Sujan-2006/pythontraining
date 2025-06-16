def checkbalance(balance):
    print(f"your balance is {balance:.2f}")
def deposit():
    amount=float(input("enter your amount: "))
    if amount<=0:
        print("amount should be greater than 0")
        return 0
    else:
        return amount

def withdraw(balance):
    amount=float(input("enter your amount to be withdrawn: "))
    if amount<0:
        print("amount should be greater than 0")
        return 0
    elif amount>balance:
        print("insufficient balance")
        return 0
    else:
        return amount


def main():
    balance=0
    running=True
    while running:
        print("----------------------")
        print("   Banking Program    ")
        print("1.Check balance")
        print("2.Deposit amount")
        print("4.Withdraw Amount")
        c=input("enter your choice : ")
        if c=='1':
            checkbalance(balance)
        elif c=='2':
            balance+=deposit()
        elif c=='3':
            balance-=withdraw(balance)
        elif c=='4':
            running =False
        else:
            print("Invalid option")
    print("Thank yo!!!")
if __name__=='__main__':
    main()

    
