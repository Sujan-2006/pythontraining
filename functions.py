import time

def count(b,a=0):     #default arguments should follow the previous
    for i in range(a,b+1):
        print(i)
        time.sleep(1)
    print("happy new year")
count(10)
count(15,5)    