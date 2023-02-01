'''
Author: Yasmine El Shafei
Check if a positive number multiple of 5 or 8
'''
def CheckNumber(n):
    if n > 0 :
        if n % 5 == 0 or n % 8 == 0:
            return True
        else:
            return False
    else:
        return False            

number = int(input("Enter Number: "))
print(CheckNumber(number))
        
