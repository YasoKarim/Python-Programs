'''
Author: Yasmine El Shafei
Find largest three numbers in a list
Sort the array in reverse order and then print first three elements
'''
list = []

size = int(input("Enter size of list: "))

for i in range(1, size + 1):
    element = int(input("Enter element: "))
    list.append(element)


list.sort(reverse=True)
print(f"List {list}")
print(f"Largest Three numbers in the list \nFirst number : " + str(list[0]) + " Second Number : " + str(list[1]) + " Third Number : " + str(list[2]) )
