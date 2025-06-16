class Bike:
    
    year=2025          #class variable
    num=0

    def __init__(self,model,color,sales):
        self.model=model          #instance variables
        self.color=color
        self.sales=sales
        Bike.num+=1

    def drive(self):
        print(f"I drive the {self.color} {self.model}")
    def stop(self):
        print(f"stop the {self.model}")