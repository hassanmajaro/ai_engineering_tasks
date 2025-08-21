''' Mixing Datatypes
    Ask the user for:
        your age (integer)
        your height in meters (float)
        your name (string)
    Print a sentence using f-string showing all details in one line,
    making sure you type-cast where necessary.
'''
age = int(input("Input your age: "))
height = float(input("Input height(m): "))
name = input("Enter your name: ")

print (f"This is {name}, {age} years old, and {height} meters tall.")