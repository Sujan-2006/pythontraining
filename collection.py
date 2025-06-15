games={"spider man":1000,
       "god of war":500,
       "gta":6000,
       "fire and water":1500}
mycart=[]
amount=0

for k,v in games.items():
    print(f"{k:20}:Rupees {v:.2f}")

while True:
    game=input("enter the game you would like to buy(press q to quit):").lower()
    if game=="q":
        break
    elif  games.get(game) is not None:
        mycart.append(game)


for game in mycart:
    amount+=games.get(game)
    print(game,end=" ")
print()
print("------------------")

print(f"total amount is {amount:.2f}")