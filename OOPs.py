'''
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

'''

class Rectangle:
    def __init__(self,width,height):
        self._width=width
        self._height=height

    @property
    def width(self):
        return f"the width is {self._width:.1f}"
    
    @property
    def height(self):
        return f"the height is {self._height:.1f}"
    
    @width.setter
    def width(self,new_width):
        if new_width>0:
            self._width=new_width
        else:
            print("width must me greater than 0")
    @height.setter
    def height(self,new_height):
        if new_height>0:
            self._height=new_height
        else:
            print("height must me greater than 0")


    @width.deleter
    def  width(self):
        del self._width
        print("Width is deleted")  

    @height.deleter
    def  height(self):
        del self._height
        print("height is deleted")  


r1=Rectangle(3,5)

r1.width=5
r1.height=7

del r1.width
del r1.height

#print(r1.width)
#print(r1.height)
