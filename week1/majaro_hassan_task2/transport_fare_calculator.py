# Transport Fare Calculator
distance = float(input("Input distance(km): "))
fare = float(input("Fare price(/km): "))

total_fare = distance * fare

print (f"The amount of total fare is {total_fare:.2f}.")