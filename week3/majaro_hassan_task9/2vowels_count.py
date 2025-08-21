'''9 
    Ask the user to enter a sentence and print the number of 
    vowels in it
'''
sen = input("Input sentence: ")
print(sen.count("a") + sen.count("e") + sen.count("i") + sen.count("o") + sen.count("u"))

sen2 = sum(sen.count(char) for char in "aeiou")
print(sen2)