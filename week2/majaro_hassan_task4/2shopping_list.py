'''2. Shopping List Manager
    Create an empty list.
    Ask the user to enter 3 shopping items (one by one)
    Add them to the list.
    Display the list as a single string, separated by commas.
'''
list = [ ]
list1 = input("Enter item 1: ")
list2 = input("Enter item 2: ")
list3 = input("Enter item 3: ")
add_list = [list1, list2, list3]
print(", ".join(add_list))