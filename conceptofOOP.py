from mainoop import Bike

b1=Bike("Harley Davidson",2025,"Black",True)
b2=Bike("Apache",2024,"yellow",False)

print(b1.model)
print(b2.year)
print(b1.color)
print(b2.sales)
b1.drive()
b2.stop()