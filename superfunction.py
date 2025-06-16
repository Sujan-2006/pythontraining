class Shape:
    def __init__(self,color,filled):
        self.color=color
        self.filled=filled
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.filled else 'not filled'}")


class Circle(Shape):
    def __init__(self,color,filled,radius):
        super().__init__(color,filled)
        self.radius=radius

    def decsribe(self):
        print(f"It is a circle with area of {3.14 * self.radius * self.radius}")
        super().describe()

class Square(Shape):
    def __init__(self,color,filled,width):
        super().__init__(color,filled)
        self.width=width
    def decsribe(self):
        print(f"It is a circle with area of {self.width * self.width}cm^2")
        super().describe()

class Triangle(Shape):
    def __init__(self,color,filled,width,height):
        super().__init__(color,filled)
        self.width=width
        self.height=height
    def decsribe(self):
        print(f"It is a circle with area of {(self.width * self.height)/2}cm^2")
        super().describe()

circle=Circle(color="Black",filled=True,radius=6)
square=Square(color="Blue",filled=False,width=5)
triangle=Triangle(color="Red",filled=False,width=5,height=7)
print(circle.color)
print(square.width)
print(triangle.height)
square.describe()