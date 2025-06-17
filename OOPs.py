class Staff:

    count=0
    tot_deg=0

    def __init__(self, name, position,noof_degree):
        self.name = name
        self.position = position
        Staff.count+=1
        Staff.tot_deg+=noof_degree


#INSTANCE METHOD
    def getinfo(self):
        return f"{self.name} = {self.position}"

    @classmethod
    def getcount(cls):   #here we use cls
        return f"Total number of Staffs: {cls.count}"
    
    @classmethod
    def get_noofdegree(cls):
        return f"Average no. of degree of all the staffs: {cls.tot_deg/cls.count}"
    
s1=Staff("Shakila","Teacher",3)
s2=Staff("Bashir","Professor",4)
s3=Staff("shanthini","HOD",5)

print(Staff.getcount())

print(Staff.get_noofdegree())

