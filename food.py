from item import Item

class Food(Item):

    def __init__(self,name:str,price:float,quantity=0,spoiledfood=0):

        #call to super function to have access to all attributes/methods
        super().__init__(
            name,price,quantity
        )
       
        assert spoiledfood>=0,f"spoiledfood count {spoiledfood} is not valid"
       

        self.spoiledfood=spoiledfood