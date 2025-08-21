''' Task5: Modify Tuple Indirectly
    Ask a user to enter three items for their shopping list
    store in a tuple shopping_list
    convert it into a list, then ask for more items to add.
    convert back to a tuple and print the updated list using join() 
    to display items separated by "|"
'''
print("===Task 5===")
shop1 = input("Enter shopping item1: ")
shop2 = input("Enter shopping item2: ")
shop3 = input("Enter shopping item3: ")
shopping_list = (shop1, shop2, shop3)
conv_list = list(shopping_list)

add_item = input("Add one more item: ")
add_item2 = input("Add another item: ")

conv_list.append(add_item)
conv_list.append(add_item2)
conv2 = tuple(conv_list)
print(" | ".join(conv2))