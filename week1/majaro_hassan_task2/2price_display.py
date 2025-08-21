''' Price Display with Type Casting
    Ask the user for the price of garri per paint in naira (as a string)
    and convert it to float. 
    Display it with a message showing the amount in naira and kobo 
    using print()
'''
print ("What is the price of garri per paint?")
price = input("Input price of garri: ")

print (f"The price of garri is {float(price):.2f}")