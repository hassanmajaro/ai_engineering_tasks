# Electricity Bill Formatter

full_name = input("Enter full name: ")
units_consumed = int(input("Enter units consumed(kWh): "))
cost_per_unit = float(input("Cost per unit: "))

total_bill = units_consumed * cost_per_unit

print ("\nCustomer Receipt")
print (f"Customer Name: \t{full_name} \nUnits consumed: {units_consumed} \nCost/Unit: \t{cost_per_unit} \nTotal bill:\t{total_bill:,}")