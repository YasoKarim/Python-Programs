'''
Author: Yasmine EL Shafei
Program for calculating the comnbination formula
Formula used: factorial(n) / (factorial(r) * factoriral(n - r))
where
n => total number of set 
r => set
To get number of ways to perform combination
or simply import comb from math library
'''
import math
def fact(n):
    f = 1
    for i in range (n , 1 , -1):
        f = f * i
    return f  
def combFunc(n,r):
    combination = fact(n) / ( fact (r) * fact(n-r) )
    print(f"Combination is {combination} \n")

n = int(input("Enter total number of set: "))
r = int(input("Enter the sample test: "))
combFunc(n,r)
#comb function
print(f"Combination Built-in function: {math.comb(n,r)}")