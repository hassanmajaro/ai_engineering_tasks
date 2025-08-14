''' Task3: Simulate a football match ticket system
    Store all seat numbers (1 to 50) in a set.
    Ask users to "book" a seat by entering the number.
    Remove booked seats from the set.
    Show remaining seats after each booking.
'''
seat_numbers = set(range(1, 51))
book = int(input("book a seat (1-50): "))
seat_numbers.remove(book)
print("Remaining seats are;", seat_numbers)