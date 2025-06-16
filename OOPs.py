class Animal:
    def __init__(self,name):
        self.name=name
        self.alive=True
    def sound(self):
        print(f"{self.name} makes sound")
    def sleep(self):
        print(f"{self.name} is sleeping")
class Dog(Animal):
    def bark(self):
        print("wooff wooff!!")
class Cat(Animal):
    def meow(self):
        print("meoowwwww!!")
    
dog=Dog("Jacky")
cat=Cat("Pinky")

print(dog.name)
print(cat.alive)
cat.sound()

dog.bark()


