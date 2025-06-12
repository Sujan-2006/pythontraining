import time

mytime = int(input("Enter time in seconds: "))
for i in range(0,mytime):
    print(i)
    time.sleep(1)
for i in range(mytime,0,-1):
    print(i)
    time.sleep(1)
print("I am SUJAN!!")