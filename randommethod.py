import random
  
#● ┌ ─ ┐ │ └ ┘        #print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")  unicode for the symbols

#   "┌─────────┐","│         │","│         │","│         │","└─────────┘"

diceart={
    1:("┌─────────┐",
       "│         │",
       "│    ●    │",
       "│         │",
       "└─────────┘"),
    2:("┌─────────┐",
       "│  ●      │",
       "│         │",
       "│      ●  │",
       "└─────────┘"),
    3:("┌─────────┐",
       "│  ●      │",
       "│    ●    │",
       "│      ●  │",
       "└─────────┘"),
    4:("┌─────────┐",
       "│  ●   ●  │",
       "│         │",
       "│  ●   ●  │",
       "└─────────┘"),
    5:("┌─────────┐",
       "│ ●     ● │",
       "│    ●    │",
       "│ ●     ● │",
       "└─────────┘"),
    6:("┌─────────┐",
       "│  ●   ●  │",
       "│  ●   ●  │",
       "│  ●   ●  │",
       "└─────────┘"),
        }

dice=[]
total=0
rolls=int(input("how many times dice rolled?"))
for die in range(rolls):
    dice.append(random.randint(1,6))
print(dice)
'''
for die in range(rolls):               #to print the dice vetrically
    for i in diceart.get(dice[die]):
        print(i)
'''
for i in range(5):
    for die in dice:                        #to print the dice horizontally
        print(diceart.get(die)[i],end=" ")
    print()

for die in dice:
    total+=die
print(f"total: {total}")
