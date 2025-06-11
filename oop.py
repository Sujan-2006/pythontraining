import csv
class item:
    all=[]

    offrate= 0.8                      #class attribute
    def __init__(self,name:str,price:float,quantity):
        assert price>=0,f"price {price} is not valid"
        assert quantity>=0,f"quantity {quantity} is not valid"
       
        self.name=name        #assigning to self object
        self.price=price 
        self.quantity=quantity

        item.all.append(self)
  
    def calculate(self):
       return self.price*self.quantity
    
    def discount(self):
        self.price=self.price * self.offrate    #initial item then self for offrate to access it from the class level

    
i1=item("phone",100,1)
i2=item("laptop",1000,3)
i3=item("caple",10,5)
i4=item("mouse",50,5)
i5=item("keyboard",70,5)

i1.discount()
print(i1.price)  #price after discount

i2.offrate=0.7
i2.discount()
print(i2.price)   #to run the calculate offrate should be self

print(i1.name) 
print(i1.price)
print(i1.quantity)
print(i2.name)
print(i2.price)
print(i2.quantity)

print(i1.calculate())
print(i2.calculate())


print(item.offrate)
print(item.__dict__)    #to see all the attributes of the class
print(i1.offrate)   #finds and prints from the class level since it is not available in the instance level
print(i2.__dict__) #to see all the attributes of the instane

print(item.all)   #only shows the address 

for instances in item.all:               #another way to print all our instances with it's values
    print(instances.name, instances.price, instances.quantity)




