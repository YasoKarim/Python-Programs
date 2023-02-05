'''
Author Name: Yasmine El Shafei
Get elements in odd position
'''
def oddPosition(list, size):
    for i in range(0,size,2):
        print(f"Element{list[i]}")
size = int(input('Enter size'))
list = []
for i in range(int(size)):
    element = int(input("Enter Element"))
    list.append(element)

oddPosition(list, size)