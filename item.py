import csv

class Item:

    offrate= 0.8
    all=[]   #class attribute
    def __init__(self,name:str,price:float,quantity=0):
        assert price>=0,f"price {price} is not valid"
        assert quantity>=0,f"quantity {quantity} is not valid"
       
        self.__name=name        #assigning to self object
        self.price=price 
        self.quantity=quantity

        Item.all.append(self)
    
    @property         #property decorator =read _only atttribute
    def name(self):
        print("blaahhhhhh")  #this will be printed when we access the name attribute
        return self.__name
    
    @name.setter     #we can rewrite the value of the name
    def name(self,val):
        if len(val)>5:
            raise Exception("looooonngggg")

        #print("ooooooooOOOOO")  #THIS WILL BE PRINTED FIRST WHEN WE SET THE VALUE TO THE ATTRIBUTE
        self.__name=val

    

    def calculate(self):
       return self.price*self.quantity
    
    def discount(self):
        self.price=self.price * self.offrate    #initial item then self for offrate to access it from the class level

    @classmethod   #class method
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader=csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
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
    
    @property
    def read_only_name(self):
        return "SUJAN"
    
Item.instantiate_from_csv()  #this will call the class method to instantiate from csv file

    