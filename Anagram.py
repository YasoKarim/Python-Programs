'''
Author: Yasmine El Shafei
check string is anagram or not
Two string said tobe anagram if thery both can be generated from each other 
'''
def checkAnagram(s1,s2):
    if(len(s1) == len(s2)):
        if(sorted(s1) == sorted(s2)):
            return True
        else:
            return False    
    else:
        return False        

word1 = input("Enter First Word: ")
word2 = input("Enter Second Word: ")
#convert to lower case
word1 = word1.lower()
word2 = word2.lower()
print(checkAnagram(word1,word2))
