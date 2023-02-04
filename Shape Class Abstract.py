'''
Author: Yasmine El Shafei
Example on Abstract Superclass Shape and Its Concrete Subclasses
Shape => Abstract class
Concrete classes => Rectangle , Circle
Exp => 6.1 
Link: https://www3.ntu.edu.sg/home/ehchua/programming/java/j3f_oopexercises.html#zz-6.1
'''
from abc import ABC ,abstractclassmethod
from cmath import pi
class Shape(ABC):
    def __init__(self, color = "red", filled = True):
        self.color = color
        self.filled = filled
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
        print(f"Shape [ Color =   {self.color}  Filled =  {self.filled} ] ")          

class Circle(Shape):
    def __init__(self, color, filled, radius = 1.0):
        Shape.__init__(self,color,filled)
        self.__radius = radius
    def getRadius(self):
        return self.__radius
    def SetRadius(self, radius):
        self.__radius = radius
    def getArea(self):
        return  pow(pi, self.__radius)
    def getPerimeter(self):
        return 2 * pi * self.__radius
    def displayCircle(self):
        print(f"Circle[ Shape [ Color =   {self.color}  Filled =  {self.filled} Radius = {self.__radius}] ]")          
      
class Rectangle(Shape):
    def __init__(self, color, filled, length  = 1.0 , width = 1.0):
        Shape.__init__(self,color,filled)
        self.__length = length
        self.__width = width
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
        print(f"Rectangle[ Shape [Color =   {self.color}  Filled =  {self.filled} Width = {self.__width} , Length = {self.__length}] ]")          
      
c1 = Circle("Color",True)      
c2 = Circle("Color",True, 2)      

r1 = Rectangle("Color",True)
r2 = Rectangle("Color",True,2,3)

c1.displayCircle()
c2.displayCircle()

r1.displayRectangle()
r2.displayRectangle()
