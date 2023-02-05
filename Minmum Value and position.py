'''
Author Name: Yasmine El Shafei
Get minimum value and it's position
'''
def minValue(list):
    minIndex = list.index(min(list))
    minValue = min(list)
    print(f"Minimum index {minIndex} Minmum value {minValue}") 

list = []
listSize = int(input("Enter size"))
for i in range(listSize):
    element = int(input("Enter Element"))
    list.append(element)
minValue(list)