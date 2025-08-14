''' Tuple Practice
    Task1: Create and Display
    Ask the user to enter three favorite Nigerian dishes (one at a time)
    Store them in a tuple called dishes
    Print the tuple in a single line, separating items with commas.
    Use the \n escape sequence to print each dish on a new line.
'''
print("===Task 1===")
dish1 = input("Input favorite dish: ")
dish2 = input("Input second fav. dish: ")
dish3 = input("Input third fav. dish: ")

dish = (dish1, dish2, dish3)

print(", ".join(dish))
print("\n".join(dish))