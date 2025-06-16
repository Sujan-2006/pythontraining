class Bike:
    def __init__(self,model,year,color,sales):
        self.model=model
        self.year=year
        self.color=color
        self.sales=sales

    def drive(self):
        print(f"I drive the {self.color} {self.model}")
    def stop(self):
        print(f"stop the {self.model}")