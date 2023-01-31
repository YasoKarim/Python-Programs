'''
Author: Yasmine El Shafei
Count vowels in a word
'''
def countVowels(s):
    count = 0
    for char in s:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            count += 1
    return count


Word = input("Enter any Word: ")
Word = Word.lower()
print(countVowels(Word))
