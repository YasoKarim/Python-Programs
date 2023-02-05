size = int(input('Enter size: '))
list2 = []
for i in range(int(size)):
    element = int(input("Enter Element: "))
    list2.append(element)

list2 = map(lambda salary : salary * 2 , list2)
print(list(list2))
     