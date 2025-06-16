from mainoop import Bike

b1=Bike("Harley Davidson","Black",True)
b2=Bike("Apache","yellow",False)
b3=Bike("TVS","green",True)

b1.drive()
b2.stop()
#print(Bike.year)
#print(Bike.num)

print(f"Our store has {Bike.num} bikes of edition {Bike.year}")
print(b1.model)
print(b2.model)
print(b3.model)