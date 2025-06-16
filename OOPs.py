class Animal:
    alive=True
class Dog(Animal):
    def sound(self):
        print("wooff!!")
class Cat(Animal):
    def sound(self):
        print("meoww!!")
class Car:        #car gets the minimm requirements ti be considered as an animal
    alive=False
    def sound(self):
        print("Honk!!")    
animals=[Dog(),Cat(),Car()]

for animal in animals:
    animal.sound()
    print(animal.alive)