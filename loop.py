#compound interest calculator 


p=0
r=0
t=0

while p<=0:
    p=float(input("enter the principle amount:"))
    if p<=0:
        print("principle amount should be greater than 0")
while r<=0:
    r=float(input("enter the rate of interest:"))
    if r<=0:
        print("rate of interest should be greater than 0")
while t<=0:
    t=float(input("enter the time period in years:"))
    if t<=0:
        print("time period should be greater than 0")

print(p)
print(r)
print(t)

amount=p*pow((1+r/100),t)
print(f"the amount after {t} years is: {amount:.2f}")