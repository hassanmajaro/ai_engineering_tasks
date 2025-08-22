''' Task3: Simulate a football match ticket system
    Store all seat numbers (1 to 50) in a set.
    Ask users to "book" a seat by entering the number.
    Remove booked seats from the set.
    Show remaining seats after each booking.
'''
seat_numbers = set(range(1, 51))
while True:
    book = int(input("Book a seat (1-50): "))

    if book > 50:
        print("Error. Seats are from 1-50")
        print("Book a new seat")
    elif book in range(1,51):
        seat_numbers.remove(book)
        print(f"Seat {book} successfully booked")
        
        book2 = int(input("book another seat: "))
        if book2 == book:
            print(f"Seat {book} has already been booked. Try again")
            print(f"Availabe seats are: {seat_numbers}")
        elif book2 in seat_numbers:
            seat_numbers.remove(book2)
            print(f"Seat {book2} successfully booked")
            print(f"Remaining seats are {seat_numbers}")
            break
    else:
        print(seat_numbers)
        

        
        
    
    # print(f"\nRemaining seats are; {seat_numbers}")

    # if book2 not in seat_numbers:
    #     print(f"Seat {book} is already booked\nBook another seat")
    #     print(f"Remaining seats are {seat_numbers}")
    
    # else:
    #     seat_numbers.remove(book2)
    #     print(f"Remaining seats are; {seat_numbers}")
# else:
#     seat_numbers.remove(book, book2)
#     print("You've booked")
# book2 = int(input("book another seat: "))