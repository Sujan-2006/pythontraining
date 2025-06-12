n=input("enter the use name:")

if(len(n)>12):
    print("name cannot be more than 12 characters")
elif not n.find(" ")==-1:
    print("name cannot contain space")
elif not n.isalnum():
    print("name cannot contain numbers")
else:
    print("name is valid")

