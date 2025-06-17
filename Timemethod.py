import time

mytime = int(input("Enter time in seconds: "))
for i in range(mytime,0,-1):
    sec=i%60
    min=int(i/60)%60
    hrs=int(i/3600)%24
    print(f"{hrs:02}:{min:02}:{sec:02}")
    time.sleep(0.1)
print("I am SUJAN!!")