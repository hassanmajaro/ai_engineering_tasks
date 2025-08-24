seat_numbers = set(range(1, 51))

while True:
    try:
        book = int(input("Book a seat (1-50): "))

        if book > 50 or book < 1:
            print("Error. Seats are from 1-50")
            print("Book a new seat")
        elif book in seat_numbers:
            seat_numbers.remove(book)
            print(f"Seat {book} successfully booked")

            try:
                book2 = int(input("Book another seat: "))

                if book2 == book:
                    print(f"Seat {book} has already been booked\nBook another seat")
                    print(f"Available seats are: {seat_numbers}")
                    break 
                elif book2 in seat_numbers:
                    seat_numbers.remove(book2)
                    print(f"Seat {book2} successfully booked")
                    print(f"Remaining seats are {seat_numbers}")
                    break
                else:
                    print(f"Seat {book2} is not available. Try again.")
            except ValueError:
                print("Invalid input. Please book seat between 1-50")
            else:
                print(f"Seat {book} is not available. Choose another seat")
                print(f"Available seats are {seat_numbers}")
    except ValueError:
        print("Invalid input. Please book a seat between 1-50")