from item import Item

class Jfood(Item):
    
    offrate = 0.7

    def __init__(self, name: str, price: float, quantity=0):
        # call to super function to have access to all attributes/methods
        super().__init__(
            name, price, quantity
        )
       




    