''' Task2: Super Market Price List
    Create a program that stores items and their prices in a dictionary
        items should come from a list.
        prices are entered by the user
        display all items and prices, then allow the user to update the price of an item.
    Requirements:
        use dictionary update method .update() or assignment.
        use .keys() to display available items
        use input validation (no advanced functions)
'''
items = ["monitor", "keyboard", "mouse", "system unit"]
item1_price = float(input("Monitor price: "))
item2_price = float(input("Keyboard price: "))
item3_price = float(input("Mouse price: "))
item4_price = float(input("System unit price: "))

store_items = {
    items[0]: (f"${item1_price}"),
    items[1]: (f"${item2_price}"),
    items[2]: (f"${item3_price}"),
    items[3]: (f"${item4_price}")
}
print(f"Store Item and prices are: {store_items}")

update_item = float(input(f"Update {items[2]} price: $"))
store_items.update({items[2] : update_item})

print(f"Available items are; {store_items.keys()}")