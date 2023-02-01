'''
Author: Yasmine El Shafei
Check if number is one of two numbers is 50 or there sum is 50
'''
def checkTwoNumber(n1,n2):
    if n1 == 50 or n2 == 50 or n1 + n2 == 50:
        return True
    else:
        return False    
number1 = int(input("Enter first number: "))        
number2 = int(input("Enter second number: "))
print(checkTwoNumber(number1, number2))        