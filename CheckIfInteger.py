'''
Author: Yasmine El Shafei
Check if number is intger or not
'''
def checkInt(n):
    if type(n) == int :
        return True
    else:
        return  False   

number = float(input("Enter Number"))
#print(isinstance(number,int))
print(checkInt(number))