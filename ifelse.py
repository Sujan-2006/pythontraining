weight=float(input("enter weight:"))                #weight converting program
unit=input("kilograms or grams(Kg or g):")
if unit=="Kg":
    weight=weight*1000
    unit="g"
elif unit=="g":
    weight=weight/1000
    unit="Kg"
else:
    print(f"{unit} is not valid")
print(f"{round(weight,2)} {unit}")