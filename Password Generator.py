'''
Author: Yasmine EL Shafei
Password generator
If it is 10 letters
60 % => 6 characters 3 (lowercase [a-z])  3 (uppercase [A-Z])
30 % => 3 digits [0-9]
10 % => 1 special charcaters [ _ | / | \ , etc...]
Module used
string 
------- 
ascci_lowercase
ascci_uppercase
digits
punctutaion -> special characters
They are lists containing all the constants instead of intilizaing a list

random -> generates entered elements in random form
-------
To import
choicing => the selected element
join.element => to concatenate the elements/element/list to the given one
sample => takes the list and it's length 
'''
import string
import random

def passwordGenerator(n):
    #Empty string to generate the new string
    newPassword = ""
    for i in range(3):
        newPassword =  newPassword + random.choice(string.ascii_lowercase)
    for i in range(3):
        newPassword =  newPassword + random.choice(string.ascii_uppercase)
    for i in range(3):
        newPassword =  newPassword + random.choice(string.digits)
    newPassword =  newPassword + random.choice(string.punctuation)
    newPassword = ''.join(random.sample(newPassword,10))        
    return newPassword
        
#number = int(input("Enter number of characters: "))    
print(passwordGenerator(10))
#print(passwordGenerator(number))