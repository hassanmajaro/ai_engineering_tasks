''' Task5: Contact Quick Lookup
    Store three names and their phone numbers in two separate tuples
        Create a dictionary from the using dict(zip(....)).
        Ask the user for a name and display the corresponding number (or an error message).
    Requirements:
        use zip() and dict() to combine tuples
        use .get() for safe retrieval
        no loops.
'''
names = ("Oba", "Ope", "David")
phone_numbers = ("23470", "23480", "23490")

details = {name: num for name, num in zip(names, phone_numbers)}
user = input("Enter name: ")
print(f"User\'s number is",details.get(user))