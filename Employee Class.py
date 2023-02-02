'''
Author: Yasmine El Shafei
Class for Employee containing:
Attributes [id , firstname , lastname , salary], Anuual Salary, Raise Salary
'''
class Employee:
    def __init__(self, id, firstname, lastname, salary):
        self.__id = id
        self.__firstname = firstname
        self.__lastname = lastname
        self.__salary = salary
    def getId(self):
        return self.__id
    def setId(self, id):
        self.__id = id        
    def getFirstname(self):
        return self.__firstname
    def getLastname(self):
        return self.__lastname
    def getSalary(self):
        return self.__salary
    def getname(self):
        return f"{self.__firtname} {self.__lastname}"
    def setSalary(self, salary):
        self.__salary = salary
    def getAnnualSalary(self):
        return self.__salary * 12 
    def raiseSalary(self, precentage):
        self.__salary =  self.__salary * precentage
        return self.__salary
    def display(self):
        print(f" Employee [ Id = {self.__id} , Name = {self.__firstname + self.__lastname} , salary = {self.__salary} ] ")
emp = Employee(10,"Yasmine", "Karim", 5000)
print(emp.getAnnualSalary())
print(emp.raiseSalary(10))
emp.display()                     
