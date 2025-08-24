'''9 
    Ask the user to enter a sentence and print the number of 
    vowels in it
'''
try:
    sen = input("Input sentence: ")
    sen2 = sum(sen.count(char) for char in "aeiou")
    print(f"No of vowels are {sen2}")
except Exception as e:
    print("An error occured: {e}")