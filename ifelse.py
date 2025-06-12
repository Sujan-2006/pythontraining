op=input("enter an operator(+,-,*,/,%):")
n1=float(input("enter value 1:"))
n2=float(input("enter value 2:"))
if op=='+':
    print(n1+n2)
elif op=='-':
    print(n1-n2)
elif op=='*':
    print(n1*n2)
elif op=='/':
    print(n1/n2)
elif op=='%':
    print(n1%n2)
else:
    print("illegal operator")

