'''
Author : Yasmine El Shafei 
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
        print(f"Person [ name = {self.name} , address = {self.address} ]")

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
        print(f"Student [Person[ name = {self.name} , address = {self.address}, program = {self.__program}, year = {self.__year} , fee = {self.__fee} ]")

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
        print(f"Staff [Person[ name = {self.name} , address = {self.address}, school = {self.__school}, pay = {self.__pay} ]")

p = Person("Yasmine" , "Egypt")
s1 = Student("Yasmine" , "Egypt", "CS", 3 , "-")
staff1 = Staff("Yasmine", "Egypt" ,"Kaumeya" ,"-")
p.displayPersonInfo()
s1.displayStudentInfo()
staff1.displayStaffInfo()
    
            