class Animal:
    def eat(self):
        print("Animals eat!!")
    
class Mammal:
    def sleep(self):
        print("Mammal sleeps!!")

class Dog(Animal,Mammal):
    def bark(self):
        print("wooff wooff!!")
dog=Dog()
dog.eat()


