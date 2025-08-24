''' Simulated USSD Menu Interaction
    You are to design a mock USSD interface for a mobile services.
    Requirements:
        1. when the user runs the program, display a welcome screen with
        a Nigerian context greeting.
        2. ask the user to "dial" a USSD code (e.g., *123#) and store it in 
        a variable.
        3. print a menu with at least 3 options (e.g., "Check Balance", 
        "Buy Airtime", "Buy Data") using newline escape squences (\n) for
        formatting.
        4. ask the user to choose an option (1, 2, or 3) and store their 
        choice in a variable.
        5. use f-strings and/or concatenation to display a confirmation
        message showing the selected option.
        6. ask for an amount (if applicable) and store it as a 
        number using type casting.
        7. display a final message summarizing the transaction.
'''
airtime_balance = 5000
data_balance = 1000
number = "09123456789"
print("Welcome to AirtelNg Services")

while True:
    ussd_code = input("Dial USSD Code: ")
    if ussd_code == "*123#":
        print("1. Check Balance\n2. Buy Airtime\n3. Buy Data")

        option = input("Reply\n")
        print(f"You selected option {option}\n")

        if option == "1":
            print("Check Balance\n1. Check Airtime Balance\n2. Check Data Balance")

            bal = input("Reply\n")

            if bal == "1":
                print(f"Your account balance is {float(airtime_balance):.2f} NGN")
                break
            elif bal == "2":
                print(f"Your data balance is {data_balance:.2f} MB")
                break 
            else:
                print("Input valid option")
                break

        elif option == "2":
            print("How much airtime do you want to purchase? ")
            buy_airtime = int(input(""))

            if buy_airtime > 10000:
                print("Sorry you can only rechage up to NGN10000 at once.\nTry again.")
            else:
                airtime_balance += buy_airtime
                print(f"Your recharge of {buy_airtime} is successful.\nYour new balance is {float(airtime_balance):,.2f}")
                break

        elif option == "3":
            print("Data Plans")
            print("1 18GB @N5000")
            print("2 10GB @N3000")
            print("3 3.5GB @N750")

            option2 = input("Reply\n")
            print(f"You selected option {option2}\n")

            if option2 == "1":
                if 5000 > airtime_balance:
                    print("Insufficient Balance.\nKindly Recharge")
                    break
                else:
                    airtime_balance -= 5000
                    data_balance += 18000
                    print(f"Your Data of 18GB @N5000 is successful")
                    print(f"Your new balance is {float(airtime_balance):.2f} NGN and your Data Balance is {data_balance:.2f} MB")
                    
                    break
            elif option2 == "2":
                if 3000 > airtime_balance:
                    print("Insufficient Balance.\nKindly Recharge")
                    break
                else:
                    airtime_balance -= 3000
                    data_balance += 10000
                    print(f"Your Data of 10GB @N3000 is successful")
                    print(f"Your new balance is {float(airtime_balance):.2f} NGN  and your Data Balance is {data_balance:.2f} MB")
                    
                    break
            elif option2 == "3":
                if 750 > airtime_balance:
                    print("Insufficient Balance.\nKindly Recharge")
                    break
                else:
                    airtime_balance -= 750
                    data_balance += 3500
                    print(f"Your Data of 3.5GB @N750 is successful")
                    print(f"Your new balance is {float(airtime_balance):.2f} NGN and your Data Balance is {data_balance:.2f} MB")
                    break
            else:
                print("Ïncorrect option.\nTry again")
        else:
            print("Input correct option!")
    else:
        print("Invalid MMI Code\nTry *123#")