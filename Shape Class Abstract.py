from abc import ABC ,abstractclassmethod
from cmath import pi
#from math import PI

class Shape(ABC):
    def __init__(self, color, filled):
        self.color = "red"
        self.filled = True
    def getcolor(self):
        return self.__color
    def SetProgram(self, color):
        self.__color = color
    def isFilled(self):
        return self.__filled 
    def setFilled(self, filled):
        self.__filled = filled
    @abstractclassmethod
    def getArea():
        pass
    def getPerimeter():
        pass
    def displayShape(self) :
        print(f"Shape [Color =   {self.color} + filled =  {self.filled} ]")          

class Circle(Shape):
    def __init__(self, color, filled, radius):
        Shape.__init__(self,color,filled)
        self.__radius = 1.0
    def getRadius(self):
        return self.__radius
    def SetRadius(self, radius):
        self.__radius = radius
    def getArea(self):
        return  pow(pi, self.__radius)
    def getPerimeter(self):
        return 2 * pi * self.__radius
    def displayRectangle(self):
        print(f"Circle[ Shape [Color =   {self.color}  filled =  {self.filled} radius = {self.__radius}]")          
      
class Rectangle(Shape):
    def __init__(self, color, filled, length, width):
        Shape.__init__(self,color,filled)
        self.__length = 1.0
        self.__width = 1.0
    def getWidth(self):
        return self.__width
    def Setwidth(self, width):
        self.__width = width
    def getLength(self):
        return self.__length
    def Setwidth(self, length):
        self.__length = length
    def getArea(self):
        return self.__length * self.__width
    def getPerimeter(self):
        return 2 * (self.__length + self.__width)
    def displayRectangle(self):
        print(f"Rectangle[ Shape [Color =   {self.color}  filled =  {self.filled} Width = {self.__width} , length = {self.__length}]")          
      
r = Rectangle("red",True,2,3)
r.displayRectangle()
