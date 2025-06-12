#shopping cart program

electronics=[]
prices=[]
totamount=0

while True:
    elec=input("enter an item you need to buy(Q to quit):")
    if elec=="Q":
        break
    else:
        price=float(input("enter the price of {elec}:"))
        electronics.append(elec)
        prices.append(price)

print("-----YOUR CART-----")
for elec in electronics:
    print(elec)

for price in prices:
    totamount+=price

print(f"Your total BILL amount is rupees {totamount:.2f}")
