'''
Author : Yasmine El Shafei
Superclass Person and its subclasses
Person class => Parent
Student and Staff class => Subclasses  
Inheritance
Exp =>  4.2
Link: https://www3.ntu.edu.sg/home/ehchua/programming/java/j3f_oopexercises.html#zz-4.2
'''
class Person:
    def __init__(self, name , address):
        self.name = name
        self.address = address
    def getName(self):
        return self.__name
    def getAddress(self):
        return self.__address
    def SetAddress(self, address):
        self.__address = address
    def displayPersonInfo(self):
        print(f"Person [ Name = {self.name} , Address = {self.address} ]")

class Student(Person):
    def __init__(self, name , address, program , year , fee):
        Person.__init__(self , name , address)
        self.__program = program
        self.__year = year
        self.__fee = fee
    def getProgram(self):
        return self.__program
    def SetProgram(self, program):
        self.__program = program
    def getYear(self):
        return self.__program
    def SetYear(self, year):
        self.__year = year
    def getFee(self):
        return self.__fee
    def SetFee(self, fee):
        self.__fee = fee
    def displayStudentInfo(self):
        print(f"Student [Person [Name = {self.name} , Address = {self.address}, Program = {self.__program}, Year = {self.__year} , Fee = {self.__fee}] ]")

class Staff(Person):
    def __init__(self, name , address, school , pay):
        Person.__init__(self, name , address)
        self.__school = school
        self.__pay = pay
    def getSchool(self):
        return self.__school
    def SetSchool(self, school):
        self.__school = school
    def getPay(self):
        return self.__pay
    def SetSchool(self, pay):
        self.__pay = pay    
    def displayStaffInfo(self):
        print(f"Staff [ Person [Name = {self.name} , Address = {self.address}, School = {self.__school}, Pay = {self.__pay}] ]")

p = Person("Name" , "Country")
student1 = Student("Name" , "Country", "Program", 2023 , "Fee")
staff1 = Staff("Name", "Country" ,"School" ,"Pay")

p.displayPersonInfo()
student1.displayStudentInfo()
staff1.displayStaffInfo()
    
            