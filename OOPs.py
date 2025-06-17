class Staff:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def getinfo(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def isvalid(position):
        valid = ["HOD", "Teacher", "Professor", "FS"]
        return position in valid
    
s1=Staff("Shakila","Teacher")
s2=Staff("Bashir","Professor")
s3=Staff("shanthini","HOD")

print(Staff.isvalid("teacher"))
print(s1.getinfo())
print(s2.getinfo())