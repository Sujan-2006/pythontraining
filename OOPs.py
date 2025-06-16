class Animal:
    def __init__(self,name):
        self.name=name

    def eat(self):
        print(f"{self.name} is an animals. It eat!!")
    
class Mammal(Animal):
    def sleep(self):
        print(f"{self.name} is a Mammal. It sleeps!!")

class Dog(Mammal):
    def bark(self):
        print("wooff wooff!!")
dog=Dog("Jacky")
dog.sleep()


