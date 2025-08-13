# Simulated USSD Menu Interaction
print ("Welcome to Airmon USSD Service")
code = input("Dial USSD code (e.g., *123#): ")
print ("Please choose an option:\n1. Buy Airtime \n2. Buy Data \n3. Check Data \n4. Manage Services")
option = int(input("Enter choice 1-4: "))
print (f"You selected option {option}")
amount = float(input("Enter amount: "))
print (f"\nYou dialled {code} for service {option} and the amount N{amount}")
print ("Thank you for using our service.")