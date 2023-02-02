class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    def getLength(self):
        return self.__length
    def setLength(self, length):
        self.__length = length        
    def getWidth(self):
        return self.__width
    def setWidth(self, width):
        self.__width = width
    def getArea(self):
        return self.__length * self.__width 
    def getPerimeter(self):
        return (self.__length + self.__width) * 2
    def displayAllInformation(self):
        print(f"Rectangle length = {self.__length}\nRectangle Width = {self.__width}\nRectangle Area = {self.getArea()}\nRectangle Perimeter {self.getPerimeter()}" )
rect = Rectangle(2,3)
rect.displayAllInformation()         