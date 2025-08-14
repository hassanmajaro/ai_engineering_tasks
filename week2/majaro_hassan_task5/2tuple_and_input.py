''' Task2: Tuple and Input
    Ask the user for 5 best friends' names.
    Store them in a tuple friends.
    Print the tupe in reverse order.
'''
print("===Task 2===")
friend1 = input("Input best friend name: ")
friend2 = input("Input 2nd best friend name: ")
friend3 = input("Input 3rd best friend name: ")
friend4 = input("Input 4th best friend name: ")
friend5 = input("Input 5th best friend name: ")
friends = (friend1, friend2, friend3, friend4, friend5)
new = list(friends)
new.reverse()
print(new)