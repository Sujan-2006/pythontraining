import random
options=("rock","paper","scissors")


while True:
    player=input("enter your choice(rock/paper/scissors)(q to quit):")
    if player=='q':
        break
    comp=random.choice(options)

       
    print(f"player: {player}")
    print(f"computer: {comp}")
    
    if player==comp:
        print("tie")
    elif player=="paper" and comp=="rock":
        print("win!")
    elif player=="rock" and comp=="scissors":
        print("win!")
    elif player=="scissors" and comp=="paper":
        print("win!")
    else:
        print("you lost!!")


print("Thanks for playing")
 