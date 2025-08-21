''' Transport Fare Calculator
    Ask for:
        distance in km (float)
        fare per km (float)
    Calculate and display the total fare with two decimal places using
    f"{value:.2f}".
'''
distance = float(input("Input distance(km): "))
fare = float(input("Fare price(p/km): "))

total_fare = distance * fare

print (f"The amount of total fare is {total_fare:.2f}.")