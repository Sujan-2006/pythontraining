class Student:
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age
    
    def __str__(self):      #string representation of the object
        return f"{self.name} is a {self.gender}"
    
    def __eq__(self,other):     #checks if it is equal or not
        return self.name==other.name and self.gender==other.gender
    
    def __lt__(self,other):    #lesser than operation
        return self.age< other.age
     
    def __add__(self,other):    #addition operation 
        return self.age+other.age
    
    def __contains__(self,key):       #check if the string present in the object
        return key in self.name or key in self.gender
    
    def __getitem__(self,key):        #to get an item(like indexing)
        if  key=="name":
            return self.name
        elif  key=="gender":
            return self.gender
        elif  key=="age":
            return self.age
        else:
            return f"{key} is not found"

s1=Student("Sujan","Male",19)
s2=Student("Mathew Emmanuel","Male",20)
s3=Student("Reshma","Female",19)
s4=Student("Vidula","Female",18)

print(s3)
print(s1==s2)
print(s2<s1)
print(s3+s4)
print("Emmanuel" in s2)
print(s4['name'])
print(s3['age'])
print(s1['manoj'])
