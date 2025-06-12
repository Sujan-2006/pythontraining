qns=("which is the most famous k-pop girl group?",
     "who is the most famous among BLACKPINK?",
     "who is the most followed Indian?",
     "who has the best voice?",
     "who is the most followed person in the world?")

ops=(("a. twice","b. blackpink","c. baby monster"),
    ("a. lisa","b. jennie","c. rose"),
    ("a. virat","b. priyanka chopra","c. aliah bhat"),
    ("a. rose ","b. ariana","c. taylor"),
    ("a. ronaldo","b. selena","c. messie"))

anss=["b","a","a","b","a"]
guesses=[]
score=0
qnno=0
for qn in qns:
    print("------------")
    print(qn)
    for op in ops[qnno]:
        print(op)
    
    guess=input("enter (a/b/c):")
    guesses.append(guess)
    if guess==anss[qnno]:
        score+=1
        print("correct")
    else:
        print("incorrect")
        print(f"{anss[qnno]} is the correct answer")
    qnno+=1

print("result------")
print("answer:",end=" ")
for ans in anss:
    print(ans,end=" ")
print()
print("guess:",end=" ")
for guess in guesses:
     print(guess,end=" ")
print()

score=(int(score/len(qns))*100)
print(f"your score is {score}%")
    
    



