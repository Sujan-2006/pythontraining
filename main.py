#hangman problem   
import random

mc=("naruto","tanjiro","light","luffy","eren")
#dictionary 
hangmanart={0:("   ",
               "   ",
               "   "),
            1:(" o ",
               "   ",
               "   "),
            2:(" o ",
               " | ",
               "   "),
            3:(" o ",
               "/| ",
               "   "),
            4:(" o ",
               "/|\\",
               "   "),
            5:(" o ",
               "/|\\",
               "/  "),
            6:(" o ",
               "/|\\",
               "/ \\")}
def disp_man(wrongguess):
   print("*********")
   for line in hangmanart[wrongguess]:
      print(line)
   print("*********")
def disp_hint(hint):
   print(" ".join(hint))
def disp_ans(answer):
   print(" ".join(answer))
def main():
   answer=random.choice(mc)
   hint=["_"]*len(answer)
   wrongguess=0
   guessed_letters=set()
   running=True
   while running:
      disp_man(wrongguess)
      disp_hint(hint)
      guess=input("enter a letter: ").lower()

      if len(guess)!=1 or not guess.isalpha():
         print("invalidn input")
         continue
        
      if guess in guessed_letters:
         print(f"{guess} is already guessed")
         continue
      guessed_letters.add(guess)
      if guess in answer:
         for i in range(len(answer)):
            if answer[i]==guess:
               hint[i]=guess
      else:
         wrongguess+=1

      if "_" not in hint:
         disp_man(wrongguess)
         disp_ans(answer)
         print("YOU WON!!")
         running=False
      elif wrongguess>=len(hangmanart)-1:
         disp_man(wrongguess)
         disp_ans(answer)
         print("YOU LOST!!")
         running=False


if __name__=='__main__':
   main()
