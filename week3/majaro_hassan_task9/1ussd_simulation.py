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
airtime_balance = 500
number = "090"
print("Welcome to AirtelNg Services")

while True:
    ussd_code = input("Dial USSD Code: ")

    if ussd_code == "*121#":
        print("1. Buy Bundles & Services")
        print("2. Manage my account")
        print("3. Borrow Credit")
        print("4. Voice Tariffs / Bundle")
        print("5. Last recharge")
        print("6. Cancel")
        
        reply = input("Reply\n")

        if reply == "1":
            print("1 Data Plans")
            print("2 18GB @N5000")
            print("3 10GB @N3000")
            print("4 3.5GB @N750")
      
            choice1 = input("Reply\n")
            if choice1 == "1":
                print("1 Daily Plans")
                print("2 Weekly Plans")
                print("3 Monthly Plans")
                print("* Exit")

                choice11 = input("Reply\n")
                if choice11 == "1":
                    print("Daily Plan")
                    print("1 N300/300MB")
                    print("2 N200/230MB")
                    print("3 N100/110MB")
                    print("4 N75/75MB")
                    print("* Exit")

                    choice111 = input("Reply\n")
                    if choice111 == "1":
                        airtime_balance -= 300
                        print(f"{choice111} Successfully Recharged.")
                        break
                    elif choice111 == "2":
                        airtime_balance -= 200
                        print(f"{choice111} Successfully Recharged.")
                        break
                    elif choice111 == "3":
                        airtime_balance -= 100
                        print(f"{choice111} Successfully Recharged.")
                        break 
                    elif choice111 == "4":
                        print(f"{choice111} Successfully Recharged.")
                        break 
                    elif choice111 == "*":
                        print("Thank you!")
                        break 
                    else:
                        print("Error. Try again")

                elif choice11 == "2":
                    print("Weekly Plan")
                    print("1 N5000/18GB")
                    print("2 N3000/10GB")
                    print("3 N2500/6GB")
                    print("* Exit")

                elif choice11 == "3":
                    print("Monthly Plan")
                    print("1 N1500/2GB")
                    print("2 N2000/3GB")
                    print("3 3000/8GB")
                    print("* Exit")

                elif choice11 == "*":
                    print("Thank you!")
                    break
                else:
                    print("Invalid option. Try again!")


            elif choice1 == "2":
                print("18GB @N5000 + 2GB YT Night+200MB YT, IG & Tiktok (7 days)")
                print("1 Buy & Auto Renew")
                print("2 Buy Once")
                print("* Exit")

            elif choice1 == "3":
                print("10GB @N3000 + 700MB YT Night+200MB YT, IG & Tiktok (7 days)")
                print("1 Buy & Auto Renew")
                print("2 Buy Once")
                print("* Exit")

            elif choice1 == "4":
                print("3.5GB @N750 + 200MB YT Night+200MB YT, IG & Tiktok (7 days)")
                print("1 Buy & Auto Renew")
                print("2 Buy Once")
                print("* Exit")

            else:
                print("Error. Try again")

        elif reply == "2":
            print("1 My Data Balance")
            print("2 My Airtime Balance")
            print("3 My Data Plan")
            print("4 Number")
            print("* Main Menu")

            choice2 = input("Reply\n")

            if choice2 == "1":
                print("Dear customer, you will receive an SMS with your Data Balance details Shortly")
                break 
            elif choice2 == "2":
                print(f"Your account balance is {float(airtime_balance):.2f} NGN")
                break 
            elif choice2 == "3":
                print("Your data plan is NA")
                break 
            elif choice2 == "4":
                print(f"Your number is {number}")
                break 
            elif choice2 == "*":
                break

        elif reply == "3":
            print("1 Borrow Credit (Welcome to Extra Credit)")
            print("2 Me2U")
            print("3 Log a complaint")
            print("* Main Menu")

            choice3 = input("Reply\n")
            if choice3 == "1":
                print("Dial *500# to borrow Airtime / Data")
                break 
            elif choice3 == "2":
                print("Service Temporary Unavailabe")
                break 
            elif choice3 == "3":
                print("Kindly visit this link https://selfcare.ng.airtel.com/LogRequest ")
                break 
            elif choice3 == "*":
                break 
            else:
                print("Invalid option")
                

        elif reply == "4":
            print("1 smartTALK @ 25k/sec flat")
            print("2 Buy Voice/Combo Bundle")
            print("* Exit")

            choice4 = input("Reply\n")
            if choice4 == "1":
                print("Diat *414# to view all Airtel voice plans")
                print("1 Cancel")
                
                option = input("Reply\n")
                if option == "1":
                    break 
                else:
                    break
            elif choice4 == "2":
                print("Service Temporarily Unavailabe")
                break
            else:
                print("Error. Try again later")
                break

        elif reply == "5":
            print("Airtel NG Message")
            print("20252208 02:43:23,1000")
            break 

        elif reply == "6":
            print("Thank you for using our service")
            break
    else:
        print("Invalid MMI Code\nTry *121#")