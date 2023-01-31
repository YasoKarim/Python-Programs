'''
Author: Yasmine EL Shafei
Program for calculating the factorial of a number
Rule : n! => exp: 5! =  1 * 2 * 3 * 4 * 5 = 120
''' 
def fact(n):
    f = 1
    for i in range (n,1,-1):
        f = f * i
    return f
number = int(input("Enter number: "))
print(f"Factorial: {fact(number)}")     
