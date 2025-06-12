import math

x=8.65
y=-19
z=3.9
#a=round(x)
#a=abs(y)
#a=max(x,y,z)
a=min(x,y,z)
print(a)

print(math.pi)
print(math.e)
print(math.sqrt(x))
print(math.ceil(x))
print(math.floor(z))



r=int(input("enter radius:"))
circumference=2*math.pi*r
area=math.pi*pow(r,2)
print(round(circumference),area)

m=int(input("enter value 1:"))
n=int(input("enter value 2:"))
o=math.sqrt(pow(m,2)+pow(n,2))
print(o)