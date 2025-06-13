import random
low=1
high=10
guesses=0
running=True
ans=random.randint(low,high)

print("NUMBER GUESSING GAME")
while running:
    guess=input("enter the guess:")
    if guess.isdigit():
        guess=int(guess)
        guesses+=1

        if guess<low or guess>high:
            print("the number you guessed is out of the range")
            print(f"please guess a number between {low} and {high}")
        elif guess<ans:
            print("you are nowhere near!!")
        elif guess>ans:
            print("you are away!!")
        else:
            print("hurrrahhhh!! you are correct ")
            print(f"no. of guesses is {guesses}")
            running=False

    else:
        print("invalid guess")
        print(f"please guess a number between {low} and {high}")