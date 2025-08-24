airtime_balance = 5000
data_balance = 1000
number = "09123456789"

print("Welcome to AirtelNg Services")

while True:
    try:
        ussd_code = input("Dial USSD code: ")
        if ussd_code == "*123#":
            print("1. Check Balance\n2. Buy Airtime\n3. Buy Data")
            
            option = input("Reply\n")
            print(f"You selected option {option}\n")

            if option == "1":
                print("Check Balance\n1. Check Airtime Balance\n2. Check Data Balance")

                bal = input("Reply\n")
                
                if bal == "1":
                    print(f"Your account balance is {float(airtime_balance):.2f} NGN")
                elif bal == "2":
                    print(f"You data balance is {float(data_balance):.2f} MB")
                    break 
                else:
                    print("Invalid input. Please Try again.")
                    continue 
            elif option == "2":
                try:
                    buy_airtime = int(input("How much airtime do you want to purchase? "))
                    if buy_airtime > 10000:
                        print("Sorry, you can only recharge up to NGN10000 at once.\nTry again.")
                        continue 
                    else:
                        airtime_balance += buy_airtime 
                        print(f"Your recharge of {buy_airtime} is successful.\nYour new balance is {float(airtime_balance):.2f}")
                        break 
                except ValueError:
                    print("Invalid amount. Please enter valid amount.")
                    continue 

            elif option == "3":
                print("Data Plans")
                print("1. 18GB @N5000")
                print("2. 10GB @N3000")
                print("3. 3.5GB @N750")

                option2 = input("Reply\n")
                print(f"You selected option {option2}\n")

                try:
                    if option2 == "1":
                        if 5000 > airtime_balance:
                            print("Insufficient Balance\nKindly Recharge")
                        else:
                            airtime_balance -= 5000
                            data_balance += 18000
                            print("Your Data of 18GB@N5000 is successful")
                            print(f"Your new balance is {float(airtime_balance):.2f} NGN and your Data balance is {float(data_balance):.2f} MB")
                            break 
                    elif option2 == "2":
                        if 3000 > airtime_balance:
                            print("Insufficient Balance\nKindly Recharrge")
                        else:
                            airtime_balance -= 3000
                            data_balance += 10000
                            print("Your Data of 10GB@N3000 is successful")
                            print(f"Your new balance is {float(airtime_balance):.2f} NGN and your Data balance is {float(data_balance):.2f} MB")
                            break 
                    elif option2 == "3":
                        if 750 > airtime_balance:
                            print("Insufficient Balance\nKindly Recharrge")
                        else:
                            airtime_balance -= 750
                            data_balance += 3500
                            print("Your Data of 3.5GB@N3500 is successful")
                            print(f"Your new balance is {float(airtime_balance):.2f} NGN and your Data balance is {float(data_balance):.2f} MB")
                            break 
                    else:
                        print("Incorrect option. Try again")
                        continue 
                except ValueError:
                    print("Invalid input. Please enter valid number")
                    continue 
                else:
                    print("Input correct option")
            else:
                print("Invalid MMI code\nTry *123#")

    except Exception as e:
        print(f"An unexpected error occured: {e}")
        continue
