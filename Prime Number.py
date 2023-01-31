'''
Author: Yasmine El Shafei
Check if a number is prime or not
A number is said to prime if it only can be divided by one and itself
Exp: 2, 3, 5, 7, 11, 13
'''
def isprime(n):
    if(n <= 1):
        print("Not prime")
    factors = 1
    for i in range(2,n+1):
        if(n % i == 0):
            factors += 1
    if(factors == 2):
        #print("Entered number is Prime")
        return True
    else:
        #print("Enterd number is not prime")    
        return False
number = int(input("Enter Number: "))
print(isprime(number))