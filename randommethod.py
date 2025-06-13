import random
options=("rock","paper","scissors")

running=True

while running:

    player=None
    comp=random.choice(options)

    while player not in options:
        player=input("enter your choice(rock/paper/scissors):")
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

    playing=input("do you waant to play_again?(y/n):").lower()
    if not playing=="y":
        running=False
print("Thanks for playing")
 