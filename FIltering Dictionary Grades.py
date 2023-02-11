'''
Author: Yasmine El Shafei
Filtering a dictonary grades
'''
def filtering_graades(pair):
    key , value = pair
    if value >= 80:
        return True
    else:
        return False    
grades = {"Yasmine" : 90 , "Mohamed" : 90 , "Karim" : 70, "Laila" : 60}
filter_grades = list((filter(filtering_graades, grades.items())))
print(filter_grades)        