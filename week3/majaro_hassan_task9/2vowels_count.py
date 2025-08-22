'''9 
    Ask the user to enter a sentence and print the number of 
    vowels in it
'''
sen = input("Input sentence: ")
sen2 = sum(sen.count(char) for char in "aeiou")
print(sen2)