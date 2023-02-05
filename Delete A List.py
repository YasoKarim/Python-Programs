'''
Author: Yasmine El Shafei
Delete list using four diffrent methods 
'''
list1 = ['1','2','3','4']
list2 = ['1','2','3','4']
list3 = ['1','2','3','4']
list4 = ['1','2','3','4']

# Using clear
print(f"List 1 Before deleting {list1}")
list1.clear()
print(f"List 1 After using clear {list2}")
# Using initialize
print(f"List 2 Before deleting {list2}")
list2 = [] 
print(f"List 2 After using clear {list2}")
# Using poping
print(f"List 3 Before deleting {list3}")
while(len(list3) != 0):
    list3.pop()
print(f"List 3 After using clear {list3}")
# Using del function
print(f"List 4 Before deleting {list4}")
del list4[:]
print(f"List 4 After using clear {list4}")