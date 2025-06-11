import csv

class Item:

    offrate= 0.8
    all=[]     
    def __init__(self,name:str,price:float,quantity=0):
        assert price>=0,f"price {price} is not valid"
        assert quantity>=0,f"quantity {quantity} is not valid"
       
        self.name=name        #assigning to self object
        self.price=price 
        self.quantity=quantity

        Item.all.append(self)
  
    def calculate(self):
       return self.price*self.quantity
    
    def discount(self):
        self.price=self.price * self.offrate    #initial item then self for offrate to access it from the class level

    @classmethod   #class method
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader=csv.DictReader(f)
            items = list(reader)
        for i in items:
            Item(
                name=i.get('name'),
                price=float(i.get('price')),
                quantity=int(i.get('quantity')),
            )
        
    @staticmethod   #static method
    def is_integer(n):
        if isinstance(n,float):
            return n.is_integer()
        elif isinstance(n,int):
            return True
        else:
            return False
 
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"   #way to print all our instances with it's values 
    
Item.instantiate_from_csv()  #this will call the class method to instantiate from csv file
print(Item.all)

print(Item.is_integer(7))


#INHERITANCE

class Food(Item):

 
    def __init__(self,name:str,price:float,quantity=0,spoiledfood=0):

        #call to super function to have access to all attributes/methods
        super().__init__(
            name,price,quantity
        )
       
        assert spoiledfood>=0,f"spoiledfood count {spoiledfood} is not valid"
       

        self.spoiledfood=spoiledfood

      

f1=Food("burger",500,5,1)
print(f1.calculate())

print(Item.all)
print(Food.all)




