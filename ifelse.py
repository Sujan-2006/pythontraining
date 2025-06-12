temperature=float(input("enter temperature:"))                #temperature conversion program
unit=input("temperature or Fahrenheit(C or F):")
if unit=="C":
    temperature=round((9*temperature)/5+32,2)
    unit="F"
elif unit=="F":
    weight=round((temperature-32)*5/9,2)
    unit="C"
else:
    print(f"{unit} is not valid")
print(f"{round(temperature,2)} {unit}")