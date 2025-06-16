import random              #PYTHON SLOT MACHINE PROGRAM

def spinrow():
    symbols=['🍇','🍊','🍎','🍉','🍌']
    return [random.choice(symbols) for _ in range(3)]
def printrow(row):
    print("---------")
    print("|".join(row))
    print("---------")
def getpayout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=='🍇':
            return bet*2
        elif row[0]=='🍊':
            return bet
        elif row[0]=='🍎':
            return bet*3
        elif row[0]=='🍉':
            return bet*5
        elif row[0]=='🍌':
            return bet*10
    return 0
def main():
    balance=1000
    print("---------------------------------")
    print("     WELCOME TO PYTHON SLOTS     ")
    print("Symbols: 🍇 🍊 🍎 🍉 🍌 ")
    print("---------------------------------")
    while balance>0:
        print(f"current blance is ${balance}")
        bet=input("Place your bet amount: ")
        if not bet.isdigit():
            print("please enter valid amount")
            continue
        bet=int(bet)
        if bet>balance:
            print("insufficient balance")
            continue
        elif bet<=0:
            print("bet amount should be greater than or equal to 0")
            continue
        
        balance-=bet

        row=spinrow()
        print("spinning....\n")
        printrow(row)

        payout=getpayout(row,bet)
        if payout>0:
            print(f"you won ${payout}")
        else:
            print("Sorry you lost this match")
        balance+=payout 

        playagain=input("do you want to spin again?(y/n) : ").lower()
        if playagain!='y':
            break
    print("*********************************************")
    print(f"GAME OVER !! YOUR FINAL BALANCE IS ${balance}")
    print("*********************************************")
        
if __name__=='__main__':
    main()
    


    
