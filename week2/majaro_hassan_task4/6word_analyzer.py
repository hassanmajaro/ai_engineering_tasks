''' # 6. Word Analyzer
    Ask the user to input a word
    Print the length of the word
    Check if it is all uppercase, all lowercase, or title case.
    reverse the word using slicing
'''
word = input("Please input a word: ")
print("length of word is", len(word))

print(word.isupper())
print(word.islower())
print(word.istitle())
print(word[::-1])