'''
Author: Yasmine El Shafei
Check if string is palindrome or not
Written from front same as back
We get the string and reverse it
'''
def checkPalindrome(string):
    # We will slice from right to left to reverse the string
    # And see if the reversed form is the same as original 
    reversedString = string[::-1]
    print(reversedString)
    if(string == reversedString):
        return True
    else:
        return False   
Word = input("Enter a word: ")
print(checkPalindrome(Word))
