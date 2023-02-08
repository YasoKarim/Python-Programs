'''
Author : Yasmine El Shafei
Program to help you choose between different options!
'''
import random 
size = int(input("Enter Size: "))
list = []
for i in range(size):
    element = input("Element: ")
    list.append(element)
print(random.choice(list))    
