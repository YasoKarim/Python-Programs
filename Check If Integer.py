'''
Author: Yasmine El Shafei
Check if number is intger or not
'''
def checkInt(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()        
number = float(input("Enter Number"))
print(checkInt(number))
