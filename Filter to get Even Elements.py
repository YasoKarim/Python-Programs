'''
Author Name: Yasmine El Shafei
Get Even elements using filter
'''
size = int(input('Enter size: '))
numbers = []
for i in range(int(size)):
    element = int(input("Enter Element: "))
    numbers.append(element)
evenNumber = filter(lambda num : num % 2 == 0, numbers)
print(list(evenNumber))