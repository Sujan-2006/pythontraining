import threading                       #MULTITHREADING->accessing multiple tasks at the same time
import time
   
def tea():
    time.sleep(6)
    print("Add the tea powder")

def water(n):
    time.sleep(5)
    print(f"Boil the water using {n}")
    
def milk():
    time.sleep(7)
    print("Pour milk in it")

c1=threading.Thread(target=water,args=("stove",))
c1.start()
c2=threading.Thread(target=tea)
c2.start()
c3=threading.Thread(target=milk)
c3.start()

c1.join()
c2.join()
c3.join()

print("The TEA is ready☕")